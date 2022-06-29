# -*- coding: utf-8 -*-
"""
Created on Mon May  9 09:46:25 2022

@author: Zahra Ghavasieh

https://www.pythonguis.com/tutorials/pyqt6-layouts/
https://doc.qt.io/qt-5/index.html
https://www.pythonguis.com/tutorials/qt-designer-gui-layout/
"""

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QVBoxLayout
from PyQt6.QtGui import QPalette, QColor



# Custom Widget to display layout colours
class Color(QWidget):

    def __init__(self, color, text=''):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)
        
        txt = QLabel(str(text))
        txt.setAlignment(Qt.Alignment.AlignCenter)
        txt.setStyleSheet("font-weight: bold; color: white")
        layout = QVBoxLayout()
        layout.addWidget(txt)
        self.setLayout(layout)
        



# Main Window
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("App Layouts")
        
        # QVBox ---------------------------------
        layout = QVBoxLayout()

        layout.addWidget(Color('red', 1))
        layout.addWidget(Color('green', 2))
        layout.addWidget(Color('blue', 3))


        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)





# MAIN
def main():
    
    app = QApplication([])
    window = MainWindow()
    window.show()
    
    app.exec()



if __name__ == '__main__':
    main() 
