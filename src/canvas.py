# -*- coding: utf-8 -*-
"""
Created on Wed Jul 13 10:32:10 2022

@author: Zahra Ghavasieh

Canvas:
    - Contains the main interface of the app
    - uses Matplotlib to create an edittable ethogram
    
Reference:
    - https://www.pythonguis.com/tutorials/pyqt6-bitmap-graphics/
"""


from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor, QPixmap
from PyQt6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QWidget, 
    QLabel, 
    QVBoxLayout, 
    QHBoxLayout,
    QGridLayout,
    QStackedLayout,
    QSlider, QSpinBox
    )





# Custom Widget to display layout colours
class Color(QWidget):

    def __init__(self, color, text=''):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)
        
        txt = QLabel(str(text))
        txt.setAlignment(Qt.AlignmentFlag.AlignCenter)
        txt.setStyleSheet("font-weight: bold; color: white")
        layout = QVBoxLayout()
        layout.addWidget(txt)
        self.setLayout(layout)
        
        
        
        
class Canvas(QWidget):
    
    timeMax = 10
    timeMin = 5
    timeStep = 1
    
    def __init__ (self):
        super().__init__()
        
        # WIDGETS ---------------------------
        
        self.image = QLabel()
        self.image.setPixmap(QPixmap('../sample_outputs/OFT June 2021_19_ganttchart.png'))
        self.image.setScaledContents(True) # resize with window
        
        self.timeMax_spinbox = QSpinBox()
        self.timeMax_spinbox.setMinimum(self.timeMin)
        self.timeMax_spinbox.setMaximum(self.timeMax)
        self.timeMax_spinbox.setSingleStep(self.timeStep)
        
        self.timeMax_slider = QSlider(Qt.Orientation.Horizontal)
        self.timeMax_slider.setMinimum(self.timeMin)
        self.timeMax_slider.setMaximum(self.timeMax)
        self.timeMax_slider.setSingleStep(self.timeStep)
        self.timeMax_slider.sliderMoved.connect(self.timeMax_slider_moved)
        
        widgets = [
            self.image,
            self.timeMax_slider,
            self.timeMax_spinbox
        ]
        
        # LAYOUT ----------------------------
        
        layout = QVBoxLayout()
        for w in widgets:
            layout.addWidget(w)

        self.setLayout(layout)
        
        
        
        
    def timeMax_slider_moved(self, p):
        self.timeMax_spinbox.setValue(p)
        
        
        
