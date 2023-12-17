# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 10:40:54 2022
@author: Zahra Ghavasieh

The File Import Window
"""


from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QAction, QIcon, QKeySequence
from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QGridLayout, QTableWidget, QTableWidgetItem, QDialogButtonBox,
    QWidget, QCheckBox, QLabel, QComboBox, QLineEdit, QSpinBox, QSizePolicy, QPushButton
)

from Constants import EZIcon
from backend.fileImportController import FileImportController
from frontend.widgets.ErrorWidget import ErrorWidget
from model.EventModel import FileEvent
from model.Enums import FileType 




class FileImportDialog(QDialog):

    def __init__(self, control: FileImportController):
        super().__init__()

        self.control = control
        errorWidget = ErrorWidget(self)
        self.control.setErrorWidget(errorWidget)

        # WINDOW ----------------------------
        
        self.setWindowTitle("File Import")
        self.setWindowIcon(QIcon(EZIcon.importEvent))
        self.setMinimumSize(QSize(800, 500))  # can't resize window now (.setFixedSize())
        self.buttonBox = QDialogButtonBox(QDialogButtonBox.StandardButton.NoButton)

        # BUTTONS -----------------------------

        cancel_btn = QPushButton("Cancel", self)
        cancel_btn.clicked.connect(self.close)
        import_btn = QPushButton("Import to Current File", self)
        import_btn.clicked.connect(self.importToCurrent_clicked)
        newFile_btn = QPushButton("Import to New File", self)
        newFile_btn.clicked.connect(self.importToNew_clicked)
        newFile_btn.setDefault(True)

        buttonBox = QDialogButtonBox(Qt.Orientation.Horizontal)
        buttonBox.addButton(cancel_btn, QDialogButtonBox.ButtonRole.RejectRole) #TODO cancel should be opposite side
        buttonBox.addButton(import_btn, QDialogButtonBox.ButtonRole.AcceptRole)
        buttonBox.addButton(newFile_btn, QDialogButtonBox.ButtonRole.AcceptRole)

        # CENTRAL WIDGET ----------------------

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(errorWidget)
        mainLayout.addWidget(FileImportWidget(self.control, parent= self))
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)


    # BUTTON EVENTS ------------------------------------------------------------
        
    def importToCurrent_clicked(self, _):
        self.control.addEventsToProject()
        self.accept()

    def importToNew_clicked(self, _):
        self.control.createNewProject()
        self.accept()


    # GETTERS ------------------------------------------------------------------
        
    def getImportedProject(self):
        return self.control.project

        


class FileImportWidget(QWidget):
    
    def __init__ (self, control: FileImportController, parent=None):
        super(QWidget, self).__init__(parent)
        self.control = control

        # TOP LAYOUT -----------------------

        topLayout = QHBoxLayout()
        formatDropDown = QComboBox()
        formatDropDown.addItems([
            str(FileType.CLEVERSYS),
            str(FileType.BORIS)
            ])
        formatDropDown.currentTextChanged.connect(lambda s: self.control.setFileType(FileType.from_str(s)))

        headerLineSpinBox = QSpinBox()
        headerLineSpinBox.setMinimum(1)
        headerLineSpinBox.setMaximum(10) #TODO: set maximum to number of lines in the file
        headerLineSpinBox.setValue(self.control.headerLine)

        topLayout.addWidget(QLabel("Format"))
        topLayout.addWidget(formatDropDown)
        topLayout.addStretch()
        topLayout.addWidget(QLabel("HeaderLine"))
        topLayout.addWidget(headerLineSpinBox)

        # TABLE LAYOUT -----------------------

        contentLayout = QHBoxLayout()

        columns = 5
        rows = len(self.control.events)
        self.table = QTableWidget(rows, columns, self)
        self.table.setHorizontalHeaderLabels(["", "Imported Name", "Shown Name", "Start", "Duration"])
        self.table.verticalHeader().hide()

        for row in range(0, rows):
            event = self.control.events[row]

            # isEnabled
            checkbox = QCheckBox(self)
            checkbox.setChecked(event.isEnabled)
            checkbox.stateChanged.connect(lambda checked, e=event: self.control.eventRowStateChanged(checked, e))
            centerCheckboxLayout = QHBoxLayout(checkbox)
            centerCheckboxLayout.setAlignment(checkbox, Qt.AlignmentFlag.AlignCenter)
            self.table.setCellWidget(row, 0, checkbox)

            # imported name
            self.table.setItem(row, 1, QTableWidgetItem(event.name))

            # Shown name TODO: change to pushbutton and add option to update all same event names
            shownName = QLineEdit()
            shownName.setText(event.shownName)
            self.table.setCellWidget(row, 2, shownName)

            # Start / Duration
            self.table.setItem(row, 3, QTableWidgetItem(str(event.start)))
            self.table.setItem(row, 4, QTableWidgetItem(str(event.length)))

        contentLayout.addWidget(self.table)
        
        # LAYOUT ----------------------------
        
        centralLayout = QVBoxLayout()
        centralLayout.addLayout(topLayout)
        centralLayout.addLayout(contentLayout)

        self.setLayout(centralLayout)