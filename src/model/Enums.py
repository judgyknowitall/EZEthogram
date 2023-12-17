# -*- coding: utf-8 -*-
"""
Created on Sat June 3 10:28:16 2023

@author: Zahra Ghavasieh

ref: https://www.pythonguis.com/tutorials/pyqt6-modelview-architecture/

Contains a number of enums
"""

from enum import Enum


# File Type used for the import window
class FileType(Enum):
    CLEVERSYS = 1
    BORIS = 2
    UNSUPPORTED = 3
    
    def __str__(self):
        match(self):
            case FileType.CLEVERSYS:
                return "CleverSys"
            case FileType.BORIS:
                return "BORIS"
            case FileType.UNSUPPORTED:
                return "Custom"
                
    @staticmethod
    def from_str(s: str):
        if s == "CleverSys":
            return FileType.CLEVERSYS
        elif s == "BORIS":
            return FileType.BORIS
        else:
            return FileType.UNSUPPORTED
