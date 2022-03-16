# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 14:00:51 2021

@author: Zahra Ghavasieh

Install Packages:
    - pip install pandas

Draws a Gantt chart per trial
Each event is on a different y-tick
"""

# eNPHR 1.0 SS_6
# runfile('C:/Aaallmine/git_repos/sandeep_matlab/boris/ganttChartEvents.py', wdir='C:/Aaallmine/git_repos/sandeep_matlab/boris', args='input.txt')

from ganttChartDrawer import draw_trial
import pandas as pd
import numpy as np
import sys



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
    df['Event'] = df['Behavior'] + ' (' + df['Modifiers'] + ')'
    
    return df




# Read and extract events
def extract_events(filename):
    print('\nExtracting events for ' + filename + '...')

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
def gantt_chart_events(filename):
    events = extract_events(filename)
    df = build_dataframe(events)
    draw_trial(filename, df)
    
    
    

# Main function
# Takes in filenames to read
def main():
    
    # You have a text file of inputs
    if (len(sys.argv) > 1):
        file = open(sys.argv[1], 'r')
        
        # Read line by line
        for line in file:
            gantt_chart_events(line.strip())
        
        file.close()
    
    
    # You didn't have a text file
    else:
        while True:
        
            # User prompt
            filename = input('Please input a File Name or q to quit: ')
            
            if filename == 'q':
                break
            
            gantt_chart_events(filename)



if __name__ == "__main__":
    main()