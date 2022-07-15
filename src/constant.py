# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 10:47:40 2022

@author: Zahra Ghavasieh

Constants
    - contains all constant variables (Icon paths)
"""


class EZIcon:
    
    iconPath = "../resources/fugue-icons-3.5.6/icons/"
    
    # Icons
    bug =  iconPath + "bug.png"
    animal = iconPath + "animal.png"
    
    
    # Instantiate to change relative path
    def __init__(self, path= iconPath):
        
        self.iconPath = path
        
        self.bug =  self.iconPath + "bug.png"
        self.animal = self.iconPath + "animal.png"

        