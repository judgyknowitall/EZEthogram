# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 20:17:32 2022

@author: Zahra Ghavasieh

Importing Events from Data files (*.csv, *.xlsx)
"""


import pandas as pd
import numpy as np

from model.BehaviourModel import Behaviour
from model.EventModel import Event


# Import XLSX file
def importCleversys(filename : str):
    # Read csv files
    df = pd.read_excel(filename, skiprows=range(0,6))
    
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
def importBoris(filename : str):
    # Read csv files
    df = pd.read_csv(filename)
    
    # TODO customize later
    # Reorganize data (concatenate behavior and modifiers)
    df['Event'] = df['Behavior'] + ' (' + df['Modifiers'] + ')'
    
    events = pd.DataFrame(df, columns=['Start (s)', 'Duration (s)', 'Event']).to_numpy()
    return events
    
   
    
# Generic Import File
def importFile(filename: str, isCleversys= False, isBoris= False):
    
    #TODO make manual instead
    isCleversys = filename.endswith('.xlsx')
    isBoris = filename.endswith('.csv')
    
    # event = [start, duration, event-name]
    events = []
    
    if isCleversys:
        events = importCleversys(filename)
        
    elif isBoris:
        events = importBoris(filename)
        
    else:
        print("Not supported yet!")
        return
        
    # Transform into [Behaviour] datatype
    behaviours = []
    for fileEvent in events:
        
        event = Event(fileEvent[0], fileEvent[1])
        
        # See if behaviour already exists -> append event instead of creating new behaviour
        behaviourIndex = -1
        for i in range(len(behaviours)):
            if behaviours[i].name == fileEvent[2]:
                behaviourIndex = i 
                break
              
        # Append Event to Behaviour
        if behaviourIndex >= 0:
            behaviours[behaviourIndex].events.append(event)
        else:
            behaviours.append(Behaviour(fileEvent[2], [event]))


    return behaviours
