# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 10:40:54 2022
@author: Zahra Ghavasieh

Main Program
"""


from PyQt6.QtCore import QSize
from PyQt6.QtGui import QAction, QPixmap
from PyQt6.QtWidgets import (
    QApplication,
    QMenu,
    QCheckBox,
    QComboBox,
    QDateEdit,
    QDateTimeEdit,
    QDial,
    QDoubleSpinBox,
    QFontComboBox,
    QLabel,
    QLCDNumber,
    QLineEdit,
    QMainWindow,
    QProgressBar,
    QPushButton,
    QRadioButton,
    QSlider,
    QSpinBox,
    QTimeEdit,
    QVBoxLayout,
    QWidget,
    QListWidget
)





# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # WINDOW ----------------------------
        
        self.setWindowTitle("Ethogram Maker")
        self.setMinimumSize(QSize(800, 500))  # can't resize window now (.setFixedSize())
        
        # WIDGETS ---------------------------
        
        timeMax_slider = QSlider()
        timeMax_slider.setMinimum(5)
        timeMax_slider.setMaximum(10)



def main():
    
    app = QApplication([])
    window = MainWindow()
    window.show()
    
    app.exec()



if __name__ == '__main__':
    main()   