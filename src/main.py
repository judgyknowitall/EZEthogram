# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 10:40:54 2022
@author: Zahra Ghavasieh

Main Program
https://www.pythonguis.com/pyqt6-tutorial/
"""


from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QIcon, QKeySequence
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QStatusBar, QToolBar
)

from EventsWindow import EventsWindow
from canvas import Canvas
from constant import EZIcon



# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        
        # WINDOW ----------------------------
        
        self.setWindowTitle("EZ Ethogram")
        self.setWindowIcon(QIcon(EZIcon.logo))   # TODO
        self.setMinimumSize(QSize(800, 500))  # can't resize window now (.setFixedSize())
        
        # Status Bar: Bottom bar that explains a QAction
        self.setStatusBar(QStatusBar(self))
        
        
        
        # QACTIONS -------------------------- #TODO action functions, icons
        
        # File actions
        newFile_action = self.createAction("New File", icon= EZIcon.newFile, function= self.onMyToolBarButtonClick)
        newFile_action.setShortcut(QKeySequence(QKeySequence.StandardKey.New))
        openFile_action = self.createAction("Open File", icon= EZIcon.openFile, function= self.onMyToolBarButtonClick)
        openFile_action.setShortcut(QKeySequence(QKeySequence.StandardKey.Open))
        saveFile_action = self.createAction("Save", icon= EZIcon.saveFile, function= self.onMyToolBarButtonClick)
        saveFile_action.setShortcut(QKeySequence(QKeySequence.StandardKey.Save))
        exportFile_action = self.createAction("Export File", icon= EZIcon.export, function= self.onMyToolBarButtonClick)
        exportFile_action.setShortcut(QKeySequence(QKeySequence.StandardKey.Print))
        
        # Edit actions
        addEvent_action = self.createAction("Add Event", icon= EZIcon.addEvent, function= self.onMyToolBarButtonClick)
        importEvent_action = self.createAction("Import Events", icon= EZIcon.importEvent, function= self.onMyToolBarButtonClick)
        editEvents_action = self.createAction("Edit Events", icon= EZIcon.editEvent, function= self.onMyToolBarButtonClick)
        editPalette_action = self.createAction("Edit Palette", icon= EZIcon.editPalette, function= self.onMyToolBarButtonClick)
        editTimeline_action = self.createAction("Edit Timeline", icon= EZIcon.timeline, function= self.onMyToolBarButtonClick)
        
        
        # View actions
        viewGrid_action = self.createAction("View Grid", function= self.onMyToolBarButtonClick)
        viewGrid_action.setCheckable(True) # Togglable
        viewEventsWindow_action = self.createAction("Events Window", function= self.toggleEventsWindow)
        viewEventsWindow_action.setCheckable(True)
        
        # Intercept signal (all connected functions will trigger!)
        #action.triggered.connect( lambda checked: self.handle_trigger(checked, <args>) )
        
        
        # MENU BAR ---------------------------
        
        # Menu Bar
        menu = self.menuBar()
        
        # File
        file_menu = menu.addMenu("&File") # Press ALT to select [File] (doesn't work on Macs)
        file_menu.addActions([newFile_action, openFile_action, saveFile_action, exportFile_action])
        
        # Edit
        edit_menu = menu.addMenu("Edit")
        edit_menu.addActions([addEvent_action, importEvent_action])
        edit_menu.addSeparator()
        edit_menu.addActions([editEvents_action, editPalette_action, editTimeline_action])
        
        # View
        view_menu = menu.addMenu("View")
        view_menu.addAction(viewEventsWindow_action)
        view_menu.addSeparator()
        view_menu.addAction(viewGrid_action)
        
        
        
        # TOOL BAR --------------------------- #TODO icons only
        
        toolbar = QToolBar("Main toolbar")
        toolbar.setIconSize(QSize(32,32))
        toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.addToolBar(toolbar)
         
        toolbar.addActions([newFile_action, openFile_action, saveFile_action, exportFile_action])
        toolbar.addSeparator()
        toolbar.addActions([importEvent_action, addEvent_action, editEvents_action])
        toolbar.addSeparator()
        toolbar.addActions([editPalette_action, editTimeline_action])
        
        
        
        # EVENTS DOCKING WINDOW -------------
        
        self.eventsWindow = EventsWindow(self)
        self.addDockWidget(
            Qt.DockWidgetArea.RightDockWidgetArea, self.eventsWindow
            )
        
        
        # CANVAS ----------------------------
        
        self.canvas = Canvas()
        self.setCentralWidget(self.canvas)
        
        
        
    # UTIL -------------------------------------------------------------------
        
    # Utility function to create a QAction
    def createAction(self, name, icon=EZIcon.bug, function=None):
        action = QAction(QIcon(icon), name, self)
        action.setStatusTip(name)
        if function != None:
            action.triggered.connect(function)
        return action
    
    
    # SLOTS ------------------------------------------------------------------
    
    def onMyToolBarButtonClick(self, s):
        print("ToolBar: click", s)
        
        
    # Toggle Events Window
    def toggleEventsWindow(self, s):
        if self.eventsWindow.isVisible():
            self.eventsWindow.setHidden(True)
        else:
            self.eventsWindow.setVisible(True)
        



if __name__ == '__main__':
    
    app = QApplication([])
    app.setStyle('Breeze')

    window = MainWindow()
    window.show()
    
    app.exec()   