# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 12:24:59 2022

@author: Zahra Ghavasieh

Behaviour Class Model
"""

from model.EventModel import Event

class Behaviour:

    def __init__(self, name: str, events: list[Event] = [], colour = (255, 255, 255, 255)):
        self.name = name            # Behaviour name
        self.events = events
        self.isVisible = True
        self.set_colour(colour)

    # Setter for colour so both versions are updated
    def set_colour(self, colour: tuple[int,int,int,int]):
        self.colour = colour                               # RGBA (0-255)
        self.plotColour = tuple(c / 255 for c in colour)    # RGBA (0-1)
