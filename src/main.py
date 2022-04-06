# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 09:52:55 2022

@author: Zahra Ghavasieh

https://www.pythonguis.com/tutorials/pyqt6-creating-your-first-window/
"""

from PyQt6.QtCore import *
from PyQt6.QtWidgets import QApplication, QWidget


# Subclass QMainWindow to customize your application's main window
'''
class MainWindow(QMainWindow):
    pass
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ethogram Maker")
        self.setFixedSize(QSize(400, 300))
        
        button = QPushButton("Press Me!")

        # Set the central widget of the Window.
        self.setCentralWidget(button)
'''


def main():
    
    app = QApplication([])
    window = QWidget()
    window.show()
    
    app.exec()



if __name__ == '__main__':
    main()    




