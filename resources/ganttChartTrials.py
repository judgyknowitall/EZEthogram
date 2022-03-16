# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 09:59:23 2021

@author: Zahra Ghavasieh

Install Packages:
    - pip install pandas

Draws a Gantt chart per trial
Each event is on a different y-tick
"""

# eNPHR 1.0 SS_6
# 

from ganttChartDrawer import draw_group
import pandas as pd
import numpy as np




# Read and organize cleversys data
def read_cleversys(filename):
    
    # Read csv files
    df = pd.read_excel('cleversys_events/Trial event export ' + filename + '.xlsx', skiprows=[0,1,2,3,4,5])
    
    # Filter out cleversys events
    filter_list = ["Mouse 1 has no movement in Area Box", "Mouse 1 Locomotion in Area Box", "Mouse 1 In Place Activity in Area Box", "Mouse 1 Grooming in Area Box"]
    result_names = ["No Movement", "Locomotion", "In Place Activity", "Grooming"]
    
    # Only take the rows where the event is mentioned in the filter list
    df = df[df["Event"].isin(filter_list)] 
    
    # Rename some cleversys events
    df["Event"].replace(dict(zip(filter_list, result_names)), inplace=True)
    
    return df




# Read and organize boris data
def read_boris(filename):
    
    # Read csv files
    df = pd.read_csv('boris_events/' + filename + ' - Zahra.csv')
    
    # Reorganize data (concatenate behavior and modifiers)
    df['Event'] = df['Behavior']  #+ ' (' + df['Modifiers'] + ')'
    
    return df




# Read and extract events
def extract_events(filename):

    # Read and organize data
    cleversys_data = read_cleversys(filename)
    boris_data = read_boris(filename)
    

    # Build list of event times [start, finish, type]
    events = pd.DataFrame(cleversys_data, columns=['From Second', 'Length(Second)', 'Event']).to_numpy()
    events2 = pd.DataFrame(boris_data, columns=['Start (s)', 'Duration (s)', 'Event']).to_numpy()

    return np.concatenate([events, events2]).transpose()





# Preprocess data and build dataframe to be fed into graph
# events = [start, length, event]
def build_dataframe(events):
    
    # Combine start & length to be a tuple => (start, length)
    bars = [(events[0][i], events[1][i]) for i in range(len(events[0]))]
    
    # Construct data frame
    df = pd.DataFrame({'Event': events[2], 'Bar': bars})    
    
    return df




# Actual main program
# Central hub
def gantt_chart_trials(filenames, trialnums):
    
    # Extract evenst of each trials
    trials = []
    for filename in filenames:
        trials.append(extract_events(filename))
    
    # Build dataframes of events per trial
    dfs = []
    for t in range(len(trials)):    
        dfs.append(build_dataframe(trials[t]))
        
    # Draw Gantt Chart
    draw_group(dfs, trialnums)
    
    
    

# Main function
# Takes in filenames to read
def main():
    
    # Open input text file
    file = open('input2.txt', 'r')
    fileInput = file.read()
    file.close()
    
    # Separate groups
    groups = fileInput.split('\n\n')
    
    for group in groups:
        lines = group.split('\n')
        trialnums = lines[0].split(',')
        gantt_chart_trials(lines[1:], trialnums)



if __name__ == "__main__":
    main()