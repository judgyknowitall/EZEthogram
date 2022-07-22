# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 12:24:59 2022

@author: Zahra Ghavasieh

Behaviour Class Model
"""

from model.EventModel import Event

class Behaviour:

    def __init__(self, name: str, events:[Event] = [], colour = "blue"):
        self.name = name    # Behaviour name
        self.events = events
        self.colour = colour
        
