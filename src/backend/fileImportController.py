# -*- coding: utf-8 -*-
"""
Created on Sat June 3 10:28:16 2023

@author: Zahra Ghavasieh

ref: https://www.pythonguis.com/tutorials/pyqt6-modelview-architecture/

ViewModel:
    - contains logic portion
"""

from frontend.widgets.ErrorWidget import ErrorWidget
from model.Enums import FileType
from model.ProjectModel import Project
from model.EventModel import FileEvent
from backend.importFile import importEventsFromFile, OrganizeIntoBehaviours



# Controller for the File Import Window
class FileImportController:
    
    def __init__(self, project: Project, fileName: str):
        self.project = project
        self.fileName = fileName
        self.fileType = FileType.CLEVERSYS
        self.headerLine = self.CLEVERSYS_HEADERLINE
        self.events: list[FileEvent] = []
        self.errors: list[str] = []
        self.errorWidget = ErrorWidget()
        self.getEventsFromFile()



    # CONSTANTS -----------------------------------------------------
    
    CLEVERSYS_HEADERLINE = 7
    BORIS_HEADERLINE = 0



    # SETTERS --------------------------------------------------------

    # Set File type and update header line based on the new file type
    # Triggers the import function after the updates
    def setFileType(self, type: FileType):
        self.clearErrors()
        self.fileType = type
        match(type):
            case FileType.CLEVERSYS:
                self.setHeaderLine(self.CLEVERSYS_HEADERLINE)
            case FileType.BORIS:
                self.setHeaderLine(self.BORIS_HEADERLINE)
            case _:
                self.addError("This file type is not supported yet!")
        self.getEventsFromFile()
    

    # Sets the header line and trigger the import function
    def setHeaderLine(self, line: int):
        self.headerLine = line
        self.getEventsFromFile()


    # Set the errors widget
    def setErrorWidget(self, widget : ErrorWidget):
        self.errorWidget = widget
    


    # ERRORS --------------------------------------------------------

    # Set errors
    def addError(self, error: str):
        self.errors.append(error)
        self.errorWidget.setErrors(self.errors)

    
    # Clear errors
    def clearErrors(self):
        self.errorWidget.clearErrors()



    # PREVIEW IMPORT FUNCTIONS ---------------------------------------
        
    # Get the events from given file
    def getEventsFromFile(self):
        try:
            self.events = importEventsFromFile(self.fileName, self.fileType, self.headerLine)
            self.clearErrors()
        except:
            self.addError("Failed to import events from the given file.")


    # Whether the file had any errors
    def hasErrors(self):
        return len(self.errors) > 0



    # UPDATE EVENT ROW FUNCTIONS -----------------------------------

    # Toggle event enabled or disabled
    def eventRowStateChanged(self, checked: bool, event: FileEvent):
        event.isEnabled = checked



    # SUBMIT FORM FUNCTIONS ---------------------------------------

    # Filter events to those enabled and organize into Behaviours
    def _getEnabledBehaviours(self):
        enabledEvents = [e for e in self.events if e.isEnabled]
        return OrganizeIntoBehaviours(enabledEvents)


    # import events to current ethogram project
    def addEventsToProject(self):
        #TODO: validate if same named events exist and show popup warning
        join = True

        behaviours = self._getEnabledBehaviours()

        if join:
            self.project.joinBehaviours(behaviours)
        else:
            self.project.behaviours.extend(behaviours)


    # import events to a new ethogram project
    def createNewProject(self):
        behaviours = self._getEnabledBehaviours()
        self.project = Project(behaviours)
    