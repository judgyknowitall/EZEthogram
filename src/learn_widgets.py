# -*- coding: utf-8 -*-
"""
Created on Thu Mar 17 09:52:55 2022

@author: Zahra Ghavasieh

https://www.pythonguis.com/tutorials/pyqt6-widgets/
https://doc.qt.io/qt-5/index.html
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
        
        self.setWindowTitle("Ethogram Maker - Learn")
        self.setMinimumSize(QSize(400, 300))  # can't resize window now (.setFixedSize())
        
        # WIDGETS ---------------------------
        
        self.button = QPushButton("Press Me!")
        self.button.setCheckable(True) #toggling button
        self.button.clicked.connect(self.the_button_was_clicked)
        self.button.clicked.connect(self.the_button_was_toggled)
        
        self.label = QLabel("click in this window")
        self.input = QLineEdit()
        #self.input.textChanged.connect(self.label.setText)
        
        self.image = QLabel()
        self.image.setPixmap(QPixmap('../sample_outputs/OFT June 2021_19_ganttchart.png'))
        self.image.setScaledContents(True) # resize with window
        
        self.comboBox = QComboBox()
        self.comboBox.addItems(['One', 'Two', 'Three'])
        self.comboBox.textActivated.connect(self.text_changed)
        self.comboBox.currentIndexChanged.connect(self.index_changed)
        self.comboBox.setEditable(True) # users can add item
        self.comboBox.setInsertPolicy(QComboBox.InsertPolicy.InsertAtBottom)
        self.comboBox.setMaxCount(10) # 10 items max
        
        listWidget = QListWidget()
        listWidget.addItems(['A', 'B', 'C'])
        
        
        widgets = [
            self.input,
            self.label,
            self.button,
            self.image,
            QCheckBox(),        # check box
            self.comboBox,      # drop down list box
            listWidget,         # list box (scrollable)
            QDial(),            # rotatable knob
            QSpinBox(),         # integer spinner
            QDoubleSpinBox(),   # a number spinner for floats
            QFontComboBox(),    # list of fonts
            QLCDNumber(),       # LCD display
            QProgressBar(),     # progress bar
            QRadioButton(),     # a toggle set, with only one active item
            QSlider(),          # slider
            QTimeEdit(),        # editting times
            QDateEdit(),        # edit dates & datetimes
            QDateTimeEdit()     # edit dates & datetimes
        ]
        
        # LAYOUT ----------------------------
        
        layout = QVBoxLayout()
        for w in widgets:
            layout.addWidget(w)

        container = QWidget()
        container.setLayout(layout)
        
        self.setCentralWidget(container)
        self.i = 0
    
        
    # SLOTS ------------------------------------------------------------------
    
    def the_button_was_clicked(self):
        self.button.setText("You already clicked me.")
        self.button.setEnabled(False)
        print("CLICKED!")

    def the_button_was_toggled(self, checked):
        print("CHECKED?", checked)
        
    def index_changed(self, i):  # i is an int    
        print(i)    
    
    def text_changed(self, s):  # s is a string
        print(s)
    
    # EVENTS -----------------------------------------------------------------
        
    def mouseMoveEvent(self, e):
        #self.setMouseTracking(True) # to track without having to click on window
        self.label.setText("mouseMoveEvent : " + str(self.i))
        self.i += 1
        # e.accept() / e.ignore() # to handle event (if ignored, event is bubbled to layout parent)
        
    # global context menu!
    def contextMenuEvent(self, e):
        context = QMenu(self)
        context.addAction(QAction("test 1", self))
        context.addAction(QAction("test 2", self))
        context.addAction(QAction("test 3", self))
        context.exec(e.globalPos())

def main():
    
    app = QApplication([])
    window = MainWindow()
    window.show()
    
    app.exec()



if __name__ == '__main__':
    main()    




