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
    behaviours : list[Behaviour] = []
    
    
    def __init__(self):
        print('Creating place holder...')
        # Place holder behaviours
        a = Behaviour('A', [Event(0.2,0.5), Event(1, 5)],(83, 121, 198, 255)) # Bottom
        b = Behaviour('B', [Event(6.2, 0.3), Event(2, 3)],(232, 171, 49, 255))
        c = Behaviour('C', [Event(0, 2), Event(4, 7)],(76, 179, 93, 255))
        
        self.behaviours = [a,b,c]
        
        
        
    def save(self):
        # TODO
        return
    
    
    
    def openProject():
        # TODO    
        
        return Project()
