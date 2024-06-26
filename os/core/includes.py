# -> PROJECT NAME : MzIn-FLnT-PTT
# -> MzIn-FLnT-PTT BRAND, VERSION : 1, DATE : 24/06/2024
#
# --- LICENSE -----------------------------------------------
#
# MIT LICENSE
#
# Copyright (c) 2024 MazeGroup Softwares / MazeGroup
# Research Institute / MazeInstance Project
#
# Permission is hereby granted, free of charge, to any
# person obtaining a copy of this software and associated 
# documentation files (the "Software"), to deal in the
# Software without restriction, including without limitation 
# the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software,
# and to permit persons to whom the Software is furnished to
# do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall
# be included in all copies or substantial portions of the
# Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY
# KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO 
# THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR
# PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE 
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF 
# CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS 
# IN THE SOFTWARE.
#
# --- CREDITS -----------------------------------------------
#
# MazeInstance Project, started by Genius_um in 2023.
# Under the name of MazeGroup. First project of organization.
# *** MazeGroup *** A French Developers Organization.
# https://mazegroup.org/
#
# *** MazeInstance *** A public domain operating system made
#                      in Python
#
# CODE BELOW WAS MADE IN 2024 BY : @Genius_um
#
# All demands in (CONTACT E-MAIL) contact@mazegroup.org /
# (Genius_um's PERSONNAL E-MAIL) geniusum.off@gmail.com

"Imports"

import importlib.util, os, sys, ctypes
from . import cases


"Classes"

class INCLUDER():
    """
    INCLUDER class will include all methods to get a flexible
    Python/C modules ecosystem and includes system.
    """

    "Exceptions defining"

    class IncluderException(BaseException): ...
    class NotExistantPath(IncluderException): ...
    class InvalidGlobals(IncluderException): ...
    class IsDirectory(IncluderException): ...
    class InvalidFileExtension(IncluderException): ...


    "Methods"
    
    def include_files(self, paths: list[str], _globals:dict) -> dict:
        """
        Include files, name format : DirnameModulename
        """

        if not isinstance(_globals, dict):
            raise self.InvalidGlobals(str(_globals))
        
        for path in paths:
            path = path.strip()

            if not os.path.exists(path):
                raise self.NotExistantPath(path)
            if os.path.isdir(path):
                raise self.IsDirectory(path)
            
            ext = os.path.splitext(os.path.basename(path))[1]
            py_ext = [".py", ".pyi", ".pyt"]
            shared_ext = [".so"]

            module_name = cases.Cases().upper_camel_case(
                os.path.splitext(
                    os.path.basename(
                        os.path.dirname(path)
                    )
                )[0] + " " +
                os.path.splitext(
                    os.path.basename(path)
                )[0]
            )

            if ext in py_ext:
                spec = importlib.util.spec_from_file_location(module_name, path)
                
                module = importlib.util.module_from_spec(spec)
                
                sys.modules[module_name] = module
                
                spec.loader.exec_module(module)
                
                _globals[module_name] = module
            elif ext in shared_ext:
                module = ctypes.CDLL(path)

                _globals[module_name] = module
    
    def include_file(self, path:str, _globals:dict) -> dict:
        """
        Include file, name format : DirnameModulename
        """

        return self.include_files([path], _globals)