# -*- coding: utf-8 -*-
"""
Created on Wed Feb  4 15:31:11 2015

@author: auh
"""

import os 

def run(**args):
        print"[*] dirlist module"
        files =os.listdir(".)
        
        return str(files)
        
        