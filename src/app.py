# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 10:40:54 2022
@author: Zahra Ghavasieh

Main Program
https://www.pythonguis.com/pyqt6-tutorial/
"""


from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QPixmap, QIcon, QKeySequence
from PyQt6.QtWidgets import (
    QApplication, QStatusBar, QMainWindow,
    QLabel, QSlider, QSpinBox,
    QVBoxLayout, QWidget,
)

from EventsWindow import EventsWindow


iconPath = "../resources/fugue-icons-3.5.6/icons/"



# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    
    timeMax = 10
    timeMin = 5
    timeStep = 1
    
    def __init__(self):
        super().__init__()
        
        # WINDOW ----------------------------
        
        self.setWindowTitle("EZ Ethogram")
        self.setMinimumSize(QSize(800, 500))  # can't resize window now (.setFixedSize())
        
        # QACTIONS -------------------------- #TODO
        
        # QAction
        button_action = QAction(QIcon(iconPath+"bug.png"),"Your button", self)
        button_action.setStatusTip("This is your button") # Explanation
        button_action.setCheckable(True) # switch instead of button
        # Qt.namespace identifiers (e.g. Qt.CTRL + Qt.Key_P)
        # or system agnostic identifiers (e.g. QKeySequence.Print)
        button_action.setShortcut(QKeySequence(QKeySequence.StandardKey.Print))
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        
        button_action2 = QAction(QIcon(iconPath+"animal.png"), "Your &button2", self)
        button_action2.setStatusTip("This is your button2")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        
        # STATUS BAR -------------------------
        
        # Status Bar: Bottom bar that explains a QAction
        self.setStatusBar(QStatusBar(self))
        
        # MENU BAR --------------------------- #TODO
        
        # Menu Bar
        menu = self.menuBar()
        
        file_menu = menu.addMenu("&File") # Press ALT to select [File] (doesn't work on Macs)
        file_menu.addAction(button_action)
        file_menu.addSeparator()
        file_menu.addAction(button_action2)
        file_submenu = file_menu.addMenu("Submenu")
        file_submenu.addAction(button_action2)
        
        edit_menu = menu.addMenu("Edit")
        
        
        view_menu = menu.addMenu("View")
        
        
        # Events Window ---------------------
        
        eventsWindow = EventsWindow(self)
        
        
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
        
            
    def onMyToolBarButtonClick(self, s):
        print("click", s)



def main():
    
    app = QApplication([])
    app.setStyle('Breeze')
    window = MainWindow()
    window.show()
    
    app.exec()



if __name__ == '__main__':
    main()   