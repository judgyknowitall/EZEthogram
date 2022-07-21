# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 15:01:09 2022

@author: Zahra Ghavasieh

Ethogram Project Class Model
"""

from model.BehaviourModel import Behaviour
from model.EventModel import Event



class Project:
    
    name = "My Ethogram"
    path = "../projects/"
    behaviours : [Behaviour] = []
    
    
    def __init__(self):
        # Place holder behaviours
        a = Behaviour('A', [Event(0.2,0.5), Event(1, 5)],"tab:green") # Bottom
        b = Behaviour('B', [Event(6.2, 0.3), Event(2, 3)],"tab:orange")
        c = Behaviour('C', [Event(0, 2), Event(4, 7)],"tab:blue")
        
        self.behaviours = [a,b,c]
        
        
        
    def save(self):
        # TODO
        return
    
    
    
    def openProject():
        # TODO    
        
        return Project()
