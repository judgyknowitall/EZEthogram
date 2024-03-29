# -*- coding: utf-8 -*-
"""
Created on Tue Jul 12 12:10:18 2022

@author: Zahra Ghavasieh

Events Window:
    - View/hide events
    - Create new events
    - Edit events
    
Reference:
    - https://doc.qt.io/qtforpython/PySide6/QtWidgets/QDockWidget.html
"""


from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QIcon, QPixmap, QColor
from PyQt6.QtWidgets import (
    QLabel, QPushButton, QVBoxLayout, QDockWidget, QGridLayout, QFrame
)

from constant import EZIcon
from backend.controller import Controller



class EventsWindow(QDockWidget):
    
     def __init__(self, control: Controller, parent=None):
         super().__init__("Events", parent)
         self.control = control
         
         # DOCK WINDOW -----------------------

         self.setBaseSize(QSize(200, 500))
         self.setMinimumSize(QSize(100,100))
         
         self.setFloating(False)
         self.setAllowedAreas(
             Qt.DockWidgetArea.BottomDockWidgetArea | 
             Qt.DockWidgetArea.LeftDockWidgetArea |
             Qt.DockWidgetArea.RightDockWidgetArea)
         self.setFeatures(
             self.DockWidgetFeature.DockWidgetMovable |
             self.DockWidgetFeature.DockWidgetFloatable
             )

         
         # WIDGETS ---------------------------
         
         events_gridLayout = QGridLayout()
         
         # TODO update this:
         row = 0
         for behaviour in self.control.project.behaviours:
             
             # View
             view_btn = QPushButton(QIcon(EZIcon.eye),'')
             view_btn.clicked.connect(lambda _, s=view_btn, b=behaviour: self.control.toggleBehaviourView(s, b))
             view_btn.setCheckable(True)
             events_gridLayout.addWidget(view_btn, row, 0)      
             
             # Colour
             pixmap = QPixmap(100,100)
             pixmap.fill(QColor(*behaviour.colour))
             clr_btn = QPushButton(QIcon(pixmap),'')
             clr_btn.clicked.connect(lambda _, s=clr_btn, b=behaviour: self.control.editBehaviourColour(s, b))
             events_gridLayout.addWidget(clr_btn, row, 1)
             
             # Behaviour Name
             events_gridLayout.addWidget(QLabel(behaviour.name), row, 2)
             row = row+1
         

         
         # LAYOUT ----------------------------
         
         layout = QVBoxLayout()
         layout.addLayout(events_gridLayout)
         
         container = QFrame()
         container.setLayout(layout)
         container.setLineWidth(2)
         self.setWidget(container)
         
         
     # SLOTS ------------------------------------------------------------------
         
     def onButtonClick(self):
         print("Events Window: click")
         
         