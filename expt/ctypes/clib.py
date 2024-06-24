import ctypes, os

dir_path = os.path.dirname(os.path.abspath(__file__))

clib = ctypes.CDLL(os.path.join(dir_path, "clib.so"))
clib.main()