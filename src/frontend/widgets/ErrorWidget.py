# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 10:40:54 2022
@author: Zahra Ghavasieh

The Error Widget
"""


from PyQt6.QtGui import QColor, QPalette
from PyQt6.QtWidgets import (QVBoxLayout,  QLabel,  QFrame)



class ErrorWidget(QFrame):

    def __init__(self, parent=None, errors:list[str] = []):
        super(ErrorWidget, self).__init__(parent)
        self.errors : list[str] = []

        self.setLineWidth(0)
        #self.setContentsMargins(0, 0, 0, 0)

        pal = self.palette()
        pal.setColor(QPalette.ColorRole.Window, QColor('red'))
        self.setPalette(pal)

        self.setErrors(errors)

        
    # Set Errors
    def setErrors(self, errors:list[str]):
        if (len(errors) == 0):
            self.clearErrors()
            return
        
        self.isVisible = True
        self.errors = errors

        layout = QVBoxLayout()
        for err in self.errors:
            label = QLabel(err)
            label.setStyleSheet('color: red')
            layout.addWidget(label)

        self.setLayout(layout)



    # Hide Widget
    def clearErrors(self):
        self.errors = []
        self.isVisible = False
