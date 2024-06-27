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

from core.paths import *
from core.includes import *
from core.utils import *
from core.compile import *


"Plan"

ProcPmp: SoonIncluded
ProcCmp: SoonIncluded
LibsSessions: SoonIncluded


"Compilation"

COMPILER().compile_shared(PATHs().join(PATHs().proc_path, "cmp.cpp"))


"Includes"

INCLUDER().include_file(PATHs().join(PATHs().proc_path, "pmp.py"), globals())
INCLUDER().include_file(PATHs().join(PATHs().proc_path, "cmp.so"), globals())
INCLUDER().include_file(PATHs().join(PATHs().libs_path, "sessions.py"), globals())


"Classes"

class RUNNER():
    def __init__(self) -> None:
        self.session = LibsSessions.Session()
        self.pmp = ProcPmp.Process()
        cmp_argv = ["", self.session.id]
        ProcCmp.main.argtypes = (ctypes.c_int, ctypes.POINTER(ctypes.c_char_p))
        ProcCmp.main.restype = None
        cmp_argc = len(cmp_argv)
        cmp_argv_conv = (ctypes.c_char_p * cmp_argc)(*map(lambda s: s.encode('utf-8'), cmp_argv))
        self.cmp = ProcCmp.main(cmp_argc, cmp_argv_conv)

    def act(self) -> None:
        ...


"Start Runner"

if __name__ == "__main__":
    RUNNER_INSTANCE: RUNNER = RUNNER()
    RUNNER_INSTANCE.act()
