# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 09:52:55 2022

@author: Zahra Ghavasieh

https://www.pythonguis.com/tutorials/pyqt6-creating-your-first-window/
https://doc.qt.io/qt-5/index.html
"""

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QLineEdit, QVBoxLayout, QWidget


# Subclass QMainWindow to customize your application's main window
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # WINDOW ----------------------------
        
        self.setWindowTitle("Ethogram Maker")
        self.setFixedSize(QSize(400, 300))  # can't resize window now (.setMinimumSize())
        
        # WIDGETS ---------------------------
        
        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True) #toggling button
        self.button.clicked.connect(self.the_button_was_clicked)
        self.button.clicked.connect(self.the_button_was_toggled)
        
        self.label = QLabel()
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)
        
        # LAYOUT ----------------------------
        
        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        layout.addWidget(self.button)
        
        container = QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)
    
        
    # SLOTS ------------------------------------------------------------------
    
    def the_button_was_clicked(self):
        self.button.setText("You already clicked me.")
        self.button.setEnabled(False)
        print("CLICKED!")

    def the_button_was_toggled(self, checked):
        print("CHECKED?", checked)


def main():
    
    app = QApplication([])
    window = MainWindow()
    window.show()
    
    app.exec()



if __name__ == '__main__':
    main()    




