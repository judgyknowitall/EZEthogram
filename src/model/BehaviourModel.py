# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 12:24:59 2022

@author: Zahra Ghavasieh

Behaviour Class Model
"""

from EventModel import Event

class Behaviour:
    
    events = []
    
    def __init__(self, name: str):
        self.name = name    # Behaviour name
        
    
    def addEvent(self, event: Event):
        self.events.append(event)