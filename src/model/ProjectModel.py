# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 15:01:09 2022

@author: Zahra Ghavasieh

Ethogram Project Class Model
"""

from model.BehaviourModel import Behaviour
from model.EventModel import Event



# Contains the entire project data needed to draw ethograms
class Project():
    
    name = "My Ethogram"
    path = "../projects/"
    behaviours : list[Behaviour] = []
    

    
    def __init__(self, behaviours:list[Behaviour] = []):
        if (len(behaviours) > 0):
            self._initializeWithBehaviours(behaviours)
        else:
            self._initializePlaceholder()



    def _initializePlaceholder(self):
        print('Creating place holder...')
        # Place holder behaviours
        a = Behaviour('A', [Event(0.2,0.5), Event(1, 5)],(83, 121, 198, 255)) # Bottom
        b = Behaviour('B', [Event(6.2, 0.3), Event(2, 3)],(232, 171, 49, 255))
        c = Behaviour('C', [Event(0, 2), Event(4, 7)],(76, 179, 93, 255))
        
        self.behaviours = [a,b,c]



    def _initializeWithBehaviours(self, behaviours:list[Behaviour]):
        print('Creating new project from imported behaviours...')
        self.behaviours = behaviours

       
    # Behaviours of the same type will be combined.
    def joinBehaviours(self, bhvrs:list[Behaviour]):
        for newBhvr in bhvrs:
            found = False
            for behaviour in self.behaviours:
                if (newBhvr.name == behaviour.name):
                    behaviour.events.extend(newBhvr.events)
                    behaviour.colour = newBhvr.colour
                    found = True
                    break
            if (not found):
                self.behaviours.append(newBhvr)
        return      
        
        

    # Save project
    def save(self):
        # TODO
        return
    
    

    # Open existing project
    def openProject():
        # TODO    
        
        return Project()
