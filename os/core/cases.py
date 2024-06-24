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

"Classes"

class Cases():
    class CasesException(BaseException): ...
    class EmptyString(CasesException): ...

    def parse_s(self, s:str) -> str:
        to_r = [*"_-+#/\\@."]
        for to_r_ in to_r:
            s = s.replace(to_r_, " ")
        s = s.lower().strip()
        if not len(s): raise self.EmptyString()
        return s

    def camel_case(self, s:str) -> str:
        s = self.parse_s
        r = ""
        for i, word in enumerate(s.split()):
            if i != 0:
                r += word.capitalize()
            else:
                r += word
        return r

    def upper_camel_case(self, s:str) -> str:
        s = self.parse_s
        r = ""
        for word in s.split():
            r += word.capitalize()
        return r
