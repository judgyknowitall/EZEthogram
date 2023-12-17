# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 12:26:03 2022

@author: Zahra Ghavasieh

Event Class Model - a more efficient model used in Behaviours
FileEvent Class Model - model used for FileImport
"""

class Event:
    
    def __init__(self, start, length):
        
        # Errors
        if (length < 0):
            raise Exception("End time is before start time!")
        
        self.start = start
        self.length = length
        

class FileEvent:
    
    def __init__(self, start, length, name):
        
        # Errors
        if (length < 0):
            raise Exception("End time is before start time!")
        
        self.name = name
        self.start = start
        self.length = length

        self.shownName = name
        self.isEnabled = True