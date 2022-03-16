# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 17:26:41 2021

@author: Zahra Ghavasieh

Install Packages:
    - pip install pandas

Counts the alternations of each event
"""



import pandas as pd
import numpy as np
from math import ceil



# Global variables
event_types = ["Grooming", "In Place Activity", "Locomotion", "No Movement", "Rearing"]



# Read and organize cleversys data
def read_cleversys(filename):
    
    # Read csv files
    df = pd.read_excel('cleversys_events/Trial event export ' + filename + '.xlsx', skiprows=[0,1,2,3,4,5])
    
    # Filter out cleversys events
    filter_list = ["Mouse 1 has no movement in Area Box", "Mouse 1 Locomotion in Area Box", "Mouse 1 In Place Activity in Area Box", "Mouse 1 Grooming in Area Box"]
    result_list = event_types[-2::-1] # reversed, without 'rearing'
    
    # Only take the rows where the event is mentioned in the filter list
    df = df[df["Event"].isin(filter_list)] 
    
    # Rename some cleversys events
    df["Event"].replace(dict(zip(filter_list, result_list)), inplace=True)
    
    return df




# Read and organize boris data
def read_boris(filename):
    
    # Read csv files
    df = pd.read_csv('boris_events/' + filename + ' - Zahra.csv')
    
    # Rename events 
    df['Event'] = event_types[-1] # 'Rearing'
    
    return df




# Read and extract events
def extract_events(filename):

    # Read and organize data
    cleversys_data = read_cleversys(filename)
    boris_data = read_boris(filename)
    

    # Build list of event times [start, finish, type]
    events = pd.DataFrame(cleversys_data, columns=['From Second', 'Event']).to_numpy()
    events2 = pd.DataFrame(boris_data, columns=['Start (s)', 'Event']).to_numpy()

    # Sort the concatenation of both list of events by start time
    out = np.concatenate([events, events2])
    out = out[out[:,0].argsort()]
    
    # Export sorted events
    with pd.ExcelWriter('out/sorted_events.xlsx', engine="openpyxl", mode='a') as writer:
        pd.DataFrame(out).to_excel(writer, 
                                   index=False, 
                                   header=['Start','Event'], 
                                   sheet_name=filename)
        
    return out.transpose()
    
    
    

# Counts and returns the alternations per event
def count_alternations(events):
    
    # events = [start, event]
    # Find and sort unique Events alphabetically
    event_list = event_types
    event_list.sort()
    event_dict = dict(zip(event_list, range(len(event_list))))
    
    # event - count of alternations per other event
    # Build empty dictionary of alternations
    alternations = dict.fromkeys(event_list)
    for event in alternations.keys():
        alternations[event] = [0] * len(event_list)
    
    # Go through list and count alternations
    for i in range(len(events[0])-1):
        
        # identify row(this event) & column(next event)
        this_event = events[1][i]
        next_event = events[1][i+1]
        
        # add to alternations
        alternations[this_event][event_dict[next_event]] += 1
        
    return pd.DataFrame(alternations)   




# Output alternation count per trial in a csv file
def output_csv(dfs):
    
    # Height of each table
    height = len(event_types) + 1
    
    with pd.ExcelWriter('out/alternation_count.xlsx') as writer:
        for df in dfs:
            
            sheet = 'Trial ' + df['trial'][0]
            
            # Header: name of video
            pd.DataFrame([df['trial'][1]]).to_excel(writer,
                                                    sheet_name = sheet,
                                                    header = False,
                                                    index = False)
            
            # Write 180 interval tables
            i = 0
            for table in df['alternations']:
                
                # calculate table row (cushion + table height)
                row = 2 * (i + 1) + height * i
                
                # Header: seconds
                from_n = i * 180
                till_n = ((i+1) * 180) - 1
                secs = [str(from_n) + ' - ' + str(till_n)]
                pd.DataFrame(secs).to_excel(writer,
                                        sheet_name = sheet,
                                        header = False,
                                        index = False,
                                        startrow = row-1)
                
                # Write table
                table.to_excel(writer, 
                                sheet_name = sheet,
                                index = False,
                                startrow = row)
        
                # increment iterator
                i += 1
        
    return




# Main function
# Uses input file to read list of videos,
# Extracts events for each video, and
# Outputs results to a csv file
def main():
    
    # Open input text file
    file = open('input3.txt', 'r')
    fileInput = file.read()
    file.close()
    
    dfs = []
    
    # line = trialnum, filename
    for line in fileInput.split('\n'):
        trial = line.split(', ')
        events = extract_events(trial[1])
        
        # Break down events to 180 sec intervals
        alternations = []
        for i in range(1, (ceil(events[0][-1]) // 180) + 1):
        
            idx_in_between = [x for x in range(len(events[0])) if events[0][x] >= (180 * (i-1)) and events[0][x] < (180 * i)]
            interval = events[:, idx_in_between]
            alternations.append(count_alternations(interval))
            
        dfs.append({'trial' : trial,'alternations' : alternations})

    output_csv(dfs)

if __name__ == "__main__":
    main()