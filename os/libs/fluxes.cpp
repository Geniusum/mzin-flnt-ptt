#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <thread>
#include <chrono>
#include <exception>
#include <stdexcept>
#include <filesystem>
#include <cctype>
#include <algorithm>

namespace fs = std::filesystem;

class FluxFile {
public:
    class FluxFileException : public std::exception { };
    class NotExistantPath : public FluxFileException { };
    class IsDirectory : public FluxFileException { };
    class FileReadingException : public FluxFileException { };
    class FileWritingException : public FluxFileException { };
    class TranslationException : public FluxFileException { };
    class FormatingException : public FluxFileException { };

    FluxFile(const std::string& path, double delay = 0) : path_(path), delay_(delay), content_(""), last_result_(nullptr) {
        if (!fs::exists(path_)) throw NotExistantPath();
        if (fs::is_directory(path_)) throw IsDirectory();
    }

    std::string try_get_content() {
        try {
            std::ifstream file(path_);
            std::stringstream buffer;
            buffer << file.rdbuf();
            return buffer.str();
        } catch (const std::exception& e) {
            throw FileReadingException();
        }
    }

    void monitoring_loop() {
        while (true) {
            content_ = try_get_content();
            if (delay_ != 0) std::this_thread::sleep_for(std::chrono::milliseconds(static_cast<int>(delay_ * 1000)));
        }
    }

    void launch_monitoring() {
        thread_ = std::thread(&FluxFile::monitoring_loop, this);
        thread_.detach();
        std::cout << "Thread started." << std::endl;
    }

    int hex_address(const std::string& address, int line_nb, bool ref = false, const std::string& active_sector = "") {
        if (!ref) {
            std::string addr = address;
            std::transform(addr.begin(), addr.end(), addr.begin(), ::toupper);
            if (addr.size() <= 2 || addr.substr(0, 2) != "0X") throw TranslationException();
            return std::stoi(addr.substr(2), nullptr, 16);
        } else {
            std::string addr = address;
            std::transform(addr.begin(), addr.end(), addr.begin(), ::toupper);
            std::string sector = active_sector;
            size_t pos = addr.find(":");
            if (pos != std::string::npos) {
                sector = addr.substr(0, pos);
                addr = addr.substr(pos + 1);
            }
            if (addr.size() <= 2 || addr.substr(0, 2) != "0X") throw TranslationException();
            int address_int = std::stoi(addr.substr(2), nullptr, 16);
            // Return as an integer; could be adapted to return a pair or a struct.
            return address_int;
        }
    }

    std::map<std::string, std::map<std::string, std::map<int, std::pair<std::string, std::string>>>> translate() {
        std::map<std::string, std::map<std::string, std::map<int, std::pair<std::string, std::string>>>> r;
        r["flux_name"] = "";
        r["sectors"] = {};

        bool started = false;
        std::string active_sector;

        std::istringstream content_stream(content_);
        std::string line;
        int line_nb = 0;
        while (std::getline(content_stream, line)) {
            line_nb++;
            line = trim(line);
            if (!line.empty()) {
                bool tag = false;
                std::string tag_content;
                if (line.front() == '[' && line.back() == ']') {
                    tag = true;
                    if (line.size() <= 2) throw TranslationException();
                    tag_content = line.substr(1, line.size() - 2);
                    std::transform(tag_content.begin(), tag_content.end(), tag_content.begin(), ::toupper);
                }
                if (tag) {
                    if (tag_content.empty()) throw TranslationException();
                    std::vector<std::string> parts = split(tag_content, ';');
                    for (const auto& part : parts) {
                        std::vector<std::string> tokens = split(part, ' ');
                        if (tokens[0] == "FLUX") {
                            if (tokens.size() != 2) throw TranslationException();
                            if (!started) {
                                started = true;
                                r["flux_name"] = tokens[1];
                            } else {
                                throw TranslationException();
                            }
                        } else if (tokens[0] == "SECTOR") {
                            if (tokens.size() != 2) throw TranslationException();
                            active_sector = tokens[1];
                            if (r["sectors"].find(active_sector) == r["sectors"].end()) {
                                r["sectors"][active_sector] = {
                                    {"size", "0"},
                                    {"cells", {}}
                                };
                            }
                        } else if (tokens[0] == "SIZE") {
                            if (active_sector.empty()) throw TranslationException();
                            if (tokens.size() != 2) throw TranslationException();
                            try {
                                int size = std::stoi(tokens[1]);
                                if (size < 0) throw TranslationException();
                                r["sectors"][active_sector]["size"] = std::to_string(size);
                            } catch (...) {
                                throw TranslationException();
                            }
                        }
                    }
                } else if (line.front() == '*') {
                    continue;
                } else {
                    std::vector<std::string> tokens = split(line, ' ');
                    if (tokens.size() < 2) throw TranslationException();
                    if (active_sector.empty()) throw TranslationException();
                    std::string address_str = tokens[0];
                    std::string type = tokens[1];
                    std::string value;
                    if (tokens.size() > 2) {
                        value = join(tokens.begin() + 2, tokens.end(), " ");
                    }
                    int address = hex_address(address_str, line_nb, false);
                    if (type == "INTEGER") {
                        try {
                            int int_value = std::stoi(value);
                            r["sectors"][active_sector]["cells"][address] = {type, std::to_string(int_value)};
                        } catch (...) {
                            throw TranslationException();
                        }
                    } else if (type == "STRING") {
                        r["sectors"][active_sector]["cells"][address] = {type, value};
                    } else if (type == "DECIMAL") {
                        try {
                            double double_value = std::stod(value);
                            r["sectors"][active_sector]["cells"][address] = {type, std::to_string(double_value)};
                        } catch (...) {
                            throw TranslationException();
                        }
                    } else if (type == "BOOLEAN") {
                        try {
                            int bool_value = std::stoi(value);
                            if (bool_value != 0 && bool_value != 1) throw TranslationException();
                            r["sectors"][active_sector]["cells"][address] = {type, std::to_string(bool_value)};
                        } catch (...) {
                            throw TranslationException();
                        }
                    } else if (type == "ADDR") {
                        std::vector<std::string> addresses = split(value, ';');
                        std::string addresses_str;
                        for (const auto& addr : addresses) {
                            if (!addr.empty()) {
                                int addr_int = hex_address(addr, line_nb, true, active_sector);
                                addresses_str += std::to_string(addr_int) + ";";
                            }
                        }
                        r["sectors"][active_sector]["cells"][address] = {type, addresses_str};
                    } else if (type == "EMPTY") {
                        r["sectors"][active_sector]["cells"][address] = {type, ""};
                    } else {
                        throw TranslationException();
                    }

                    if (r["sectors"][active_sector]["size"] != "0" && r["sectors"][active_sector]["cells"].size() > std::stoi(r["sectors"][active_sector]["size"])) {
                        throw TranslationException();
                    }
                }
            }
        }

        if (!started) throw TranslationException();

        last_result_ = r;
        return r;
    }

    std::string format(const std::map<std::string, std::map<std::string, std::map<int, std::pair<std::string, std::string>>>>& flux_trace) {
        std::ostringstream s;
        s << "[FLUX " << flux_trace.at("flux_name") << "]\n";
        for (const auto& sector : flux_trace.at("sectors")) {
            s << "[SECTOR " << sector.first << "; SIZE " << sector.second.at("size") << "]\n";
            for (const auto& cell : sector.second.at("cells")) {
                std::string address = "0x" + to_hex(cell.first);
                s << "    " << address << " " << cell.second.first << " " << cell.second.second << "\n";
            }
        }
        return s.str();
    }

    void write_file(const std::string& path, const std::string& content) {
        try {
            std::ofstream file(path);
            file << content;
        } catch (const std::exception& e) {
            throw FileWritingException();
        }
    }

    void write_file_dir(const std::string& name, const std::string& content) {
        try {
            std::string directory = fs::path(path_).parent_path();
            std::ofstream file(fs::path(directory) / name);
            file << content;
        } catch (const std::exception& e) {
            throw FileWritingException();
        }
    }
            
private:
    std::string path_;
    double delay_;
    std::string content_;
    std::thread thread_;
    std::map<std::string, std::map<std::string, std::map<int, std::pair<std::string, std::string>>>> last_result_;

    // Utility functions
    std::string trim(const std::string& s) {
        auto start = s.begin();
        while (start != s.end() && std::isspace(*start)) start++;
        auto end = s.end();
        do { end--; } while (std::distance(start, end) > 0 && std::isspace(*end));
        return std::string(start, end + 1);
    }

    std::vector<std::string> split(const std::string& s, char delimiter) {
        std::vector<std::string> tokens;
        std::string token;
        std::istringstream tokenStream(s);
        while (std::getline(tokenStream, token, delimiter)) {
            tokens.push_back(token);
        }
        return tokens;
    }

    std::string join(std::vector<std::string>::iterator begin, std::vector<std::string>::iterator end, const std::string& delimiter) {
        std::ostringstream result;
        if (begin != end) result << *begin++;
        while (begin != end) result << delimiter << *begin++;
        return result.str();
    }

    std::string to_hex(int num) {
        std::ostringstream ss;
        ss << std::hex << num;
        return ss.str();
    }
};

int main() {
    try {
        FluxFile ins("out.flx", 0.5);
        ins.content = ins.try_get_content();
        auto result = ins.translate();
        std::string formatted = ins.format(result);
        ins.write_file_dir("out2.flx", formatted);
    } catch (const std::exception& e) {
        std::cerr << "An error occurred: " << e.what() << std::endl;
    }

    return 0;
}
