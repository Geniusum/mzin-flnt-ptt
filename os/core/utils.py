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

import uuid, random


"Classes"

class SoonIncluded():
    """
    A class for initialize names of modules not even
    included.
    """

class ChangeableByUser():
    """
    A class who say at the user he can change the value.
    """

class SoonUsed():
    """
    A class for initialize variables without use it at the
    moment.
    """

class IDs():
    def generate_MzV1_XXL(self):
        _ = [*str(uuid.uuid4()).replace(":", "").replace("-", "")]
        random.shuffle(_)
        __ = [*str(uuid.uuid4()).replace(":", "").replace("-", "")]
        _ = [*"".join(_) + "".join(__)]
        random.shuffle(_)
        _ = "".join(_)
        return _

    def generate_MzV1_XL(self):
        r = self.generate_MzV1_XXL()
        return r[:32]
    
    def generate_MzV1_L(self):
        r = self.generate_MzV1_XL()
        return r[:16]
    
    def generate_MzV1_M(self):
        r = self.generate_MzV1_L()
        return r[:8]
    
    def generate_MzV1_S(self):
        r = self.generate_MzV1_M()
        return r[:6]
    
    def generate_MzV1_XS(self):
        r = self.generate_MzV1_S()
        return r[:4]
    
    def generate_MzV1_XXS(self):
        r = self.generate_MzV1_XS()
        return r[:2]