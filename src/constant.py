# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 10:47:40 2022

@author: Zahra Ghavasieh

Constants
    - contains all constant variables (Icon paths)
"""


class EZIcon:
    
    oldIconPath = "../resources/fugue-icons-3.5.6/icons/"
    iconPath = "./assets/"
    ext = ".svg"
    
    # Icons
    bug =  oldIconPath + "bug.png"
    animal = oldIconPath + "animal.png"
    
    logo = iconPath + "logo" + ext
    title = iconPath + "EZEthogram" + ext
    
    newFile = iconPath + "newFile" + ext
    openFile = iconPath + "openFile" + ext
    saveFile = iconPath + "saveFile" + ext
    
    importEvent = iconPath + "import" + ext
    export = iconPath + "export" + ext
    
    addEvent = iconPath + "addEvent" + ext
    editEvent = iconPath + "editEvent" + ext
    editPalette = iconPath + "editPalette" + ext
    timeline = iconPath + "timeline" + ext
    
    eye = iconPath + "eye" + ext
    crossedEye = iconPath + "crossedEye" + ext
    square = iconPath + "square" + ext
    
    palette = iconPath + "palette" + ext
    
    
    # Instantiate to change relative path
    def __init__(self, path= oldIconPath, useSVG= True):
        
        self.oldIconPath = path
        
        self.bug =  self.oldIconPath + "bug.png"
        self.animal = self.oldIconPath + "animal.png"
        
        
        # extension
        if not useSVG:
            self.ext = ".png"
            
            
        # build icon paths
        self.logo = self.iconPath + "logo" + self.ext
        self.title = self.iconPath + "EZEthogram" + self.ext
        
        self.newFile = self.iconPath + "newFile" + self.ext
        self.openFile = self.iconPath + "openFile" + self.ext
        self.saveFile = self.iconPath + "saveFile" + self.ext
        
        self.importEvent = self.iconPath + "import" + self.ext
        self.export = self.iconPath + "export" + self.ext
        
        self.addEvent = self.iconPath + "addEvent" + self.ext
        self.editEvent = self.iconPath + "editEvent" + self.ext
        self.editPalette = self.iconPath + "editPalette" + self.ext
        self.timeline = self.iconPath + "timeline" + self.ext
        
        self.eye = self.iconPath + "eye" + self.ext
        self.crossedEye = self.iconPath + "crossedEye" + self.ext
        self.square = self.iconPath + "square" + self.ext
        
        self.palette = self.iconPath + "palette" + self.ext

 

class FileFormat:
        
    svg = "Scalable Vector Graphics (*.svg)"
    png = "Portable Network Graphic (*.png)"
    pdf = "Portable Document Format (*.pdf)"
    ps = "Postscript (*.ps)"
    eps = "Encapsulated PostScript (*.eps)"





       