# -*- coding: utf-8 -*-
"""
Created on Thu Jun 30 12:25:13 2022

@author: Zahra Ghavasieh

https://www.pythonguis.com/tutorials/pyqt6-actions-toolbars-menus/
"""


from PyQt6.QtWidgets import (
    QMainWindow, QApplication,
    QLabel, QToolBar, QStatusBar, QCheckBox
)
from PyQt6.QtGui import QAction, QIcon, QKeySequence
from PyQt6.QtCore import QSize, Qt

iconPath = "../resources/fugue-icons-3.5.6/icons/"

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Toolsbars and Menus")
        
        # The `Qt` namespace has a lot of attributes to customize
        # widgets. See: http://doc.qt.io/qt-5/qt.html
        label = QLabel("Hello!")
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        self.setCentralWidget(label)
        
        # Toolbar
        toolbar = QToolBar("Main toolbar")
        toolbar.setIconSize(QSize(16,16))
        toolbar.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)
        
        self.addToolBar(toolbar)
        
        # QAction
        button_action = QAction(QIcon(iconPath+"bug.png"),"Your button", self)
        button_action.setStatusTip("This is your button") # Explanation
        button_action.setCheckable(True) # switch instead of button
        # Qt.namespace identifiers (e.g. Qt.CTRL + Qt.Key_P)
        # or system agnostic identifiers (e.g. QKeySequence.Print)
        button_action.setShortcut(QKeySequence(QKeySequence.StandardKey.Print))
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        toolbar.addAction(button_action)
        
        toolbar.addSeparator()
        
        button_action2 = QAction(QIcon(iconPath+"animal.png"), "Your &button2", self)
        button_action2.setStatusTip("This is your button2")
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action2.setCheckable(True)
        toolbar.addAction(button_action2)
        
        toolbar.addWidget(QLabel("Label"))
        toolbar.addWidget(QCheckBox())
        
        # Status Bar: Bottom bar that explains a QAction
        self.setStatusBar(QStatusBar(self))
        
        # Menu Bar
        menu = self.menuBar()
        
        file_menu = menu.addMenu("&File") # Press ALT to select [File] (doesn't work on Macs)
        file_menu.addAction(button_action)
        file_menu.addSeparator()
        file_menu.addAction(button_action2)
        
        file_submenu = file_menu.addMenu("Submenu")
        file_submenu.addAction(button_action2)
        
        
    def onMyToolBarButtonClick(self, s):
        print("click", s)



# MAIN
def main():
    
    app = QApplication([])
    window = MainWindow()
    window.show()
    
    app.exec()



if __name__ == '__main__':
    main() 
