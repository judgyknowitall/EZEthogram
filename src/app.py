# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 10:40:54 2022
@author: Zahra Ghavasieh

Main Program
"""


from PyQt6.QtCore import QSize, Qt
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
    
    timeMax = 10
    timeMin = 5
    timeStep = 1
    
    def __init__(self):
        super().__init__()
        
        # WINDOW ----------------------------
        
        self.setWindowTitle("Ethogram Maker")
        self.setMinimumSize(QSize(800, 500))  # can't resize window now (.setFixedSize())
        
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

        container = QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)
        
        
    # SLOTS ------------------------------------------------------------------
    
    def timeMax_slider_moved(self, p):
        self.timeMax_spinbox.setValue(p)



def main():
    
    app = QApplication([])
    window = MainWindow()
    window.show()
    
    app.exec()



if __name__ == '__main__':
    main()   