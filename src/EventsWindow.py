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
         super().__init__(parent)
         self.setWindowTitle("Events")
         
         self.newEvent_btn = QPushButton(QIcon(iconPath+"calculator--plus.png"), "New Event")
         
         widgets = [
             self.newEvent_btn
             ]
         
         # LAYOUT ----------------------------
         
         layout = QVBoxLayout()
         for w in widgets:
             layout.addWidget(w)
         
         self.setLayout(layout) #TODO: doesn't show
         