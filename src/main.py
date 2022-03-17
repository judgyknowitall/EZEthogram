# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 09:52:55 2022

@author: Zahra Ghavasieh

https://www.pythonguis.com/tutorials/pyqt6-creating-your-first-window/
"""

import sys

from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


# Subclass QMainWindow to customize your application's main window
'''
class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ethogram Maker")
        self.setFixedSize(QSize(400, 300))
        
        button = QPushButton("Press Me!")

        # Set the central widget of the Window.
        self.setCentralWidget(button)
'''

def main():
    
    
    #QQuickWindow.setSceneGraphBackend('software')
    
    app = QGuiApplication(sys.argv)
    
    engine = QQmlApplicationEngine()
    engine.quit.connect(app.quit)
    engine.load('main.qml')
    win = engine.rootObjects()[0]
    win.show()

    sys.exit(app.exec())
    '''
    app = QApplication([])
    window = MainWindow()
    window.show()
    
    app.exec()
'''


if __name__ == '__main__':
    main()    
