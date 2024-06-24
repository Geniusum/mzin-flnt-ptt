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

import importlib.util, os
from . import cases


"Classes"

class INCLUDER():
    """
    INCLUDER class will include all methods to get a flexible
    Python modules ecosystem and includes system.
    """

    "Exceptions defining"

    class IncluderException(BaseException): ...
    class NotExistantPath(IncluderException): ...


    "Methods"
    
    def include_files(self, paths:list[str]) -> None:
        for path in paths:
            path = path.strip()
            if not os.path.exists(path):
                raise self.NotExistantPath(path)
            module_name = cases.Cases().upper_camel_case(os.path.splitext(os.path.basename(os.path.dirname(path)))[0] + " " + os.path.splitext(os.path.basename(path))[0])
            spec = importlib.util.spec_from_file_location(module_name, path)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(globals())            
