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
from PyQt6.QtGui import QAction, QPixmap, QIcon, QKeySequence
from PyQt6.QtWidgets import (
    QApplication, QStatusBar, QMainWindow,
    QLabel, QSlider, QSpinBox, QPushButton,
    QVBoxLayout, QWidget, QDockWidget, QGridLayout, QFrame
)

from constant import EZIcon


class IconWidget(QWidget):
    def __init__(self, icon= EZIcon.bug):
        super().__init__()
        
        ic = QLabel()
        ic.setPixmap(QPixmap(icon).scaled(16,16,Qt.AspectRatioMode.KeepAspectRatio))
        #ic.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        layout = QVBoxLayout()
        layout.addWidget(ic)
        self.setLayout(layout)



class EventsWindow(QDockWidget):
     def __init__(self, parent=None):
         super().__init__("Events", parent)
         
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
         
         events_desc = [
             "Rearing (U)", "Rearing (S)", "No Movement", 
             "Locomotion", "In Place Activity", "Grooming"
             ]
         

         events_gridLayout = QGridLayout()
         
         row = 0
         for event in events_desc:
             #TODO: make icon buttons instead
             events_gridLayout.addWidget(IconWidget(icon= EZIcon.eye), row, 0)      # View
             events_gridLayout.addWidget(IconWidget(icon= EZIcon.square), row, 1)   # Colour
             events_gridLayout.addWidget(QLabel(event), row, 2)                     # Behaviour name
             row = row+1
         
         
         newEvent_btn = QPushButton(QIcon(EZIcon.bug), "New Event")
         newEvent_btn.clicked.connect(self.onButtonClick)
         
         
         widgets = [
             newEvent_btn
             ]
         
         # LAYOUT ----------------------------
         
         layout = QVBoxLayout()
         layout.addLayout(events_gridLayout)
         for w in widgets:
             layout.addWidget(w)
         
         container = QFrame()
         container.setLayout(layout)
         container.setLineWidth(2)
         self.setWidget(container)
         
         
     # SLOTS ------------------------------------------------------------------
         
     def onButtonClick(self):
         print("Events Window: click")
         
         