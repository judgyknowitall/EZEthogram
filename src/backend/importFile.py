# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 20:17:32 2022

@author: Zahra Ghavasieh

Importing Events from Data files (*.csv, *.xlsx)
"""


import pandas as pd
from model.Enums import FileType
from model.BehaviourModel import Behaviour
from model.EventModel import Event, FileEvent


# Import XLSX file
def importCleversys(filename : str, headerline: int):
    # Read csv files
    skipMax = max(0, headerline - 1)
    df = pd.read_excel(filename, skiprows=range(0,skipMax))
    
    # TODO customize later
    # Filter out cleversys events
    filter_list = ["Mouse 1 has no movement in Area Box", "Mouse 1 Locomotion in Area Box", "Mouse 1 In Place Activity in Area Box", "Mouse 1 Grooming in Area Box"]
    result_names = ["No Movement", "Locomotion", "In Place Activity", "Grooming"]
    
    # Only take the rows where the event is mentioned in the filter list
    df = df[df["Event"].isin(filter_list)] 
    
    # Rename some cleversys events
    df["Event"].replace(dict(zip(filter_list, result_names)), inplace=True)
    events = pd.DataFrame(df, columns=['From Second', 'Length(Second)', 'Event']).to_numpy()
    
    return events




# Import Boris CSV file
def importBoris(filename : str, headerline: int):
    # Read csv files
    skipMax = max(0, headerline - 1)
    df = pd.read_csv(filename, skiprows=range(0, skipMax))
    
    # TODO customize later
    # Reorganize data (concatenate behavior and modifiers)
    df['Event'] = df['Behavior'] + ' (' + df['Modifiers'] + ')'
    
    events = pd.DataFrame(df, columns=['Start (s)', 'Duration (s)', 'Event']).to_numpy()
    return events
    

   
    
# Creates a list of events imported from file
def importEventsFromFile(filename: str, type: FileType, headerline: int) -> list[FileEvent]:
    
    # event = [start, duration, event-name]
    events = []
    
    match type:
        case FileType.CLEVERSYS:
            events = importCleversys(filename, headerline)
        
        case FileType.BORIS:
            events = importBoris(filename, headerline)

        case _:
            print("Not supported yet!")
            return
        
    return [FileEvent(e[0], e[1], e[2]) for e in events]



# Organizes a list of file events into behaviours
def OrganizeIntoBehaviours(fileEvents: list[FileEvent]) -> list[Behaviour]:
    # Transform into [Behaviour] datatype
    behaviours = []
    for fileEvent in fileEvents:
        
        event = Event(fileEvent.start, fileEvent.length)
        
        # See if behaviour already exists -> append event instead of creating new behaviour
        behaviourIndex = -1
        for i in range(len(behaviours)):
            if behaviours[i].name == fileEvent.shownName:
                behaviourIndex = i 
                break
              
        # Append Event to Behaviour
        if behaviourIndex >= 0:
            behaviours[behaviourIndex].events.append(event)
        else:
            behaviours.append(Behaviour(fileEvent.shownName, [event]))

    return behaviours