# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 21:34:24 2022

@author: Zahra Ghavasieh

https://www.pythonguis.com/tutorials/pyqt6-creating-multiple-windows/
"""

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget
from random import randint



# For temporary windows (plots, outputs)
class AnotherWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        self.label = QLabel("Another Window % d" % randint(0,100))
        layout.addWidget(self.label)
        self.setLayout(layout)




class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        
        self.w = None               # Toggling window
        self.w2 = AnotherWindow()   # Persistent window
        
        button = QPushButton("Push to Toggle Window")
        button.clicked.connect(self.toggle_window)
        button2 = QPushButton("Push for Persistent Window")
        button2.clicked.connect(
            lambda checked: self.toggle_window(self.w2)
        )
        
        layout = QVBoxLayout()
        layout.addWidget(button)
        layout.addWidget(button2)
        
        container = QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)


    def toggle_window(self, checked):
        
        if self.w is None:
            self.w = AnotherWindow() # Must be a class variable to persist window
            self.w.show()
          
        # Toggle window
        else:  
            self.w.close()  # Close Window
            self.w = None   # Discard reference
            
            
    def toggle_window(self, window):
        if window.isVisible():
            window.hide()

        else:
            window.show()



def main():
    
    app = QApplication([])
    window = MainWindow()
    window.show()
    
    app.exec()



if __name__ == '__main__':
    main()   