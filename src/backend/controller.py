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
from constant import FileFormat, EZIcon

from PyQt6.QtGui import QIcon, QPixmap, QColor
from PyQt6.QtWidgets import (
    QFileDialog, QColorDialog, QPushButton
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
    def export(self, s, parent=None):
        imagePath = self.project.path + self.project.name
        fileFormats = ";; ".join([FileFormat.png, FileFormat.pdf, FileFormat.ps, FileFormat.eps, FileFormat.svg])
        fname = QFileDialog.getSaveFileName(parent, 'Save Ethogram', imagePath, fileFormats, FileFormat.svg)
        if fname[0]:
            self.ethogram.exportPlot(fname[0])
        
        
        
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
        self.ethogram.viewGrid(s)
        
    
    # Show / hide Events-Window
    def toggleEventsWindow(self, eventsWindow):
        if eventsWindow.isVisible():
            eventsWindow.setHidden(True)
        else:
            eventsWindow.setVisible(True)
            
            
    
    # EVENTS WINDOW FUNCTIONS ------------------
    
    
    # Toggle view of the behaviour
    def toggleBehaviourView(self, source:QPushButton, behaviour:Behaviour):

        if (source.isChecked()):
            source.setIcon(QIcon(EZIcon.crossedEye))
        else:
            source.setIcon(QIcon(EZIcon.eye))

        behaviour.isVisible = not source.isChecked()
        self.ethogram.drawPlot(self.project)
    
    
    # Change the Behaviour colour
    def editBehaviourColour(self, source:QPushButton, behaviour:Behaviour):
        col = QColorDialog.getColor()
        if col.isValid():
            rgba = col.getRgb()
            pixmap = QPixmap(100,100)
            pixmap.fill(QColor(*rgba))
            source.setIcon(QIcon(pixmap))
            
            behaviour.set_colour(rgba)
            self.ethogram.drawPlot(self.project)

        
        
        
    # CANVAS FUNCTIONS --------------------------
    
    
    def setPlot(self, parent=None):
        self.ethogram = EthogramPlot(parent)
        self.ethogram.drawPlot(self.project)
    
    
    
    
    def onMyToolBarButtonClick(self, s):
        print("ToolBar: click", s)
        
        
        