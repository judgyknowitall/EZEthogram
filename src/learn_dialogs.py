# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 19:13:41 2022

@author: Zahra Ghavasieh

https://www.pythonguis.com/tutorials/pyqt6-dialogs/
"""


from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QDialog,
    QPushButton, QDialogButtonBox, QMessageBox,
    QVBoxLayout, QLabel, QWidget
    )



class CustomDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("HELLO!")
        
        QBtn = QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox. accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        
        self.layout = QVBoxLayout()
        message = QLabel("Something happened, is that OK?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)
        
        


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Learn Dialogs")

        button = QPushButton("Press me for a dialog!")
        button.clicked.connect(self.button_clicked)
        button2 = QPushButton("Press me for a messagebox!")
        button2.clicked.connect(self.button2_clicked)
        button3 = QPushButton("Don't Press me!")
        button3.clicked.connect(self.button3_clicked)
        
        layout = QVBoxLayout()
        layout.addWidget(button)
        layout.addWidget(button2)
        layout.addWidget(button3)
        
        container = QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)


    # Show Custom Dialog
    def button_clicked(self, s):        
        dlg = CustomDialog(self)
        if dlg.exec():
            print("SUCCESS")
        else:
            print("CANCEL")
            
     
    # Show Message Box
    def button2_clicked(self, s):
        # Can replace the lines below with built in dialog:
        # button = QMessageBox.question(self, "Qestion Dialog", "The Longer Message")
        # Built in Dialogs: information, question, warning, critical
        dlg = QMessageBox(self)
        dlg.setWindowTitle("I have a question!")
        dlg.setText("This is a question dialog")
        dlg.setStandardButtons(QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        dlg.setIcon(QMessageBox.Icon.Question)
        button = dlg.exec()

        if button == QMessageBox.StandardButton.Yes:
            print("Yes!")
        else:
            print("No!")
            
            
    # Critical
    def button3_clicked(self, s):
        button = QMessageBox.critical(
            self,
            "Oh dear!",
            "Something went very wrong.",
            buttons=QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.NoToAll | QMessageBox.StandardButton.Ignore,
            defaultButton=QMessageBox.StandardButton.Discard,
        )

        if button == QMessageBox.StandardButton.Discard:
            print("Discard!")
        elif button == QMessageBox.StandardButton.NoToAll:
            print("No to all!")
        else:
            print("Ignore!")



# MAIN
def main():
    
    app = QApplication([])
    window = MainWindow()
    window.show()
    
    app.exec()



if __name__ == '__main__':
    main() 

