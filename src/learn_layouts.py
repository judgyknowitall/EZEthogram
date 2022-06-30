# -*- coding: utf-8 -*-
"""
Created on Mon May  9 09:46:25 2022

@author: Zahra Ghavasieh

https://www.pythonguis.com/tutorials/pyqt6-layouts/
https://doc.qt.io/qt-5/index.html
https://www.pythonguis.com/tutorials/qt-designer-gui-layout/
"""

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import (
    QApplication, 
    QMainWindow, 
    QWidget, 
    QLabel, 
    QVBoxLayout, 
    QHBoxLayout,
    QGridLayout,
    QStackedLayout
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



# Main Window
class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("App Layouts")
        
        
        # QVBox ---------------------------------
        vert_layout = QVBoxLayout()

        vert_layout.addWidget(Color('red', 'V1'))
        vert_layout.addWidget(Color('green', 'V2'))
        vert_layout.addWidget(Color('blue', 'V3'))
        
        # QHBox ---------------------------------
        horizon_layout = QHBoxLayout()
        horizon_layout.addWidget(Color('yellow', 'H1'))
        horizon_layout.addWidget(Color('cyan', 'H2'))
        horizon_layout.addWidget(Color('magenta', 'H3'))
        
        # QGridLayout ---------------------------
        grid_layout = QGridLayout() # can skip grid slots
        grid_layout.addWidget(Color('purple', 'G1'), 0, 0)
        grid_layout.addWidget(Color('orange', 'G2'), 1, 2)
        grid_layout.addWidget(Color('brown', 'G3'), 2, 1)
        
        # QStackedLayout ------------------------ (can be used for tabs)
        stack_layout = QStackedLayout()
        s1 = Color('black', 'S1')
        s2 = Color('gray', 'S2')
        stack_layout.addWidget(s1) # first element is shown by default
        stack_layout.addWidget(s2)
        #stack_layout.setCurrentIndex(1) # can set either index/widget
        s1.mousePressEvent = lambda e:stack_layout.setCurrentWidget(s2)
        s2.mousePressEvent = lambda e:stack_layout.setCurrentWidget(s1)
        
        # Central Layout ------------------------
        cent_layout = QVBoxLayout()
        cent_layout.addLayout(vert_layout)
        cent_layout.addLayout(horizon_layout)
        cent_layout.addLayout(grid_layout)
        cent_layout.addLayout(stack_layout)
        
        cent_layout.setContentsMargins(5,5,5,5) # set spacing around layout
        cent_layout.setSpacing(0)               # space between (ALL) elements


        widget = QWidget()
        widget.setLayout(cent_layout)
        self.setCentralWidget(widget)

        




# MAIN
def main():
    
    app = QApplication([])
    window = MainWindow()
    window.show()
    
    app.exec()



if __name__ == '__main__':
    main() 
