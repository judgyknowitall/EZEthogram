# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 15:54:16 2022

@author: Zahra Ghavasieh

ref: https://www.pythonguis.com/tutorials/pyqt6-modelview-architecture/

ViewModel:
    - contains logic portion
"""

from model.ProjectModel import Project
from model.BehaviourModel import Behaviour
from frontend.ethogramPlot import EthogramPlot



class Controller:
    
    def __init__(self):
        self.project = Project()
        self.ethogram:EthogramPlot = None
    


    # FILE FUNCTIONS ---------------------------
    
    def newFile(self, s):
        print("NEW FILE!") # TODO
        
    
    def openFile(self, s):
        print("OPEN FILE!") # TODO
    
    
    def saveFile(self, s):
        print("SAVE FILE") # TODO
    
    
    def importEvents(self, s):
        print("IMPORT EVENTS!") # TODO
    
    
    def export(self, s):
        print("EXPORT!") # TODO
        
        
        
    # EDIT FUNCTIONS ---------------------------   
     
     
    def addEvent(self, s):
         print("ADD EVENT") #TODO
         
     
    def editEvents(self, s):
        print("EDIT EVENTS") #TODO
        
    
    def editPalette(self, s):
        print("EDIT PALETTE") #TODO
        
        
    def editTimeline(self, s):
        print("EDIT TIMELINE") #TODO
        
        
        
    # VIEW FUNCTIONS ---------------------------  
     
     
    def viewGrid(self, s):
        print("VIEW GRID?", s) #TODO
        
    
    def toggleEventsWindow(self, eventsWindow):
        if eventsWindow.isVisible():
            eventsWindow.setHidden(True)
        else:
            eventsWindow.setVisible(True)
            
            
    
    # EVENTS WINDOW FUNCTIONS ------------------
    
    
    def toggleBehaviourView(self, s, behaviour:Behaviour):
        print("TOGGLE BEHAVIOUR:", behaviour.name) #TODO
    
    
    def editBehaviourColour(self, behaviour:Behaviour):
        print("EDIT BEHAVIOUR:", behaviour.name) #TODO
        
    
    def newEvent(self, s):
        print("NEW EVENT") #TODO
        
        
        
    # CANVAS FUNCTIONS --------------------------
    
    
    def setPlot(self, parent=None):
        self.ethogram = EthogramPlot(parent)
        self.ethogram.drawPlot(self.project)
    
    
    def onMyToolBarButtonClick(self, s):
        print("ToolBar: click", s)
        
        
        