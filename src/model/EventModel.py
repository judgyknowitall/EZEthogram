# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 12:26:03 2022

@author: Zahra Ghavasieh

Event Class Model
"""

class Event:
    
    def __init__(self, start, length):
        
        # Errors
        if (length < 0):
            raise Exception("End time is before start time!")
        
        self.start = start
        self.length = length
        