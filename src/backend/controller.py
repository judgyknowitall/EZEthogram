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
from backend.importFile import importFile

from PyQt6.QtWidgets import (
    QFileDialog, QColorDialog
)



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
        # QFileDialog.getSaveFileName()
    
    
    # Import Events from a data(csv/xlsx) file
    def importEvents(self, s, parent=None):
        fname = QFileDialog.getOpenFileName(parent, 'Open File', self.project.path, 'Data File (*.csv; *.xlsx)')
        if fname[0]:
            self.project.behaviours = importFile(fname[0]) #TODO append later
            self.ethogram.drawPlot(self.project) # update plot
    
    
    # Export Plot
    def export(self, s):
        self.ethogram.exportPlot(self.project.name, outputPath= self.project.path)
        
        
        
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
        
    
    # Show / hide Events-Window
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
        col = QColorDialog.getColor()
        if col.isValid():
            print(col.getRgb())
        
    
    def newEvent(self, s):
        print("NEW EVENT") #TODO
        
        
        
    # CANVAS FUNCTIONS --------------------------
    
    
    def setPlot(self, parent=None):
        self.ethogram = EthogramPlot(parent)
        self.ethogram.drawPlot(self.project)
    
    
    def onMyToolBarButtonClick(self, s):
        print("ToolBar: click", s)
        
        
        