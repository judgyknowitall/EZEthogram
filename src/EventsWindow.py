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

iconPath = "../resources/fugue-icons-3.5.6/icons/"


from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QPixmap, QIcon, QKeySequence
from PyQt6.QtWidgets import (
    QApplication, QStatusBar, QMainWindow,
    QLabel, QSlider, QSpinBox, QPushButton,
    QVBoxLayout, QWidget, QDockWidget
)

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
         
         newEvent_btn = QPushButton(QIcon(iconPath+"calculator--plus.png"), "New Event")
         newEvent_btn.clicked.connect(self.onButtonClick)
         
         
         widgets = [
             newEvent_btn
             ]
         
         # LAYOUT ----------------------------
         
         layout = QVBoxLayout()
         for w in widgets:
             layout.addWidget(w)
         
         container = QWidget()
         container.setLayout(layout)
         self.setWidget(container)
         
         
         # SLOTS ------------------------------------------------------------------
         
         def onButtonClick(self, s):
             print("Events Window: click", s)
         
         