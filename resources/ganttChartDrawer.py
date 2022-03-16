# -*- coding: utf-8 -*-
"""
Created on Fri Aug 27 12:05:33 2021

@author: Zahra Ghavasieh

Draws a Gantt chart given params
"""

# Importing the matplotlib.pyplot
import matplotlib.pyplot as plt


# Colours used for bars in chart
clrs = [
        #'black',           # Groom
        'tab:orange',       # In Place Activity
        'tab:green',        # Locomotion
        'tab:red',          # No Movement
        'tab:purple',       # Rear
        'tab:brown',
        'tab:pink',
        'tab:gray',
        'tab:olive',
        'tab:cyan'
        ]


# Draw a single trial with each event on its own axis
# xmax set to 9 minutes (540 seconds)
# x = (x_start, x_len)
# y = Event name
def draw_trial(filename, df, x="Bar", y="Event", xmax=540, sort=True):
    
    print("Drawing Gantt Chart...")
 
    # Declaring figure and its aspect ratio
    plt.figure(figsize=(20,8))
    
    
    # Find and sort unique Events alphabetically
    events = list(set(df[y]))
    if sort:
        events.sort()
     
    # Set limits
    plt.ylim(0, len(events)*10)
    plt.xlim(0, xmax)
     
    # Setting axis labels
    plt.xlabel('Time (s)')
     
    # Setting ticks on y-axis
    plt.yticks([ (i*10)+5 for i in range(len(events))], events)


    # Setting ticks on x-axis
    plt.xticks(range(0,xmax+1,60))

     
    # Setting graph attribute
    #plt.grid(True,axis='x')
    
    # Declare bars in chart
    for i in range(len(events)):
        
        # Get all occurrences of the event and draw its bars
        occurrences = df[df[y] == events[i]] 
        print("\t- Found " + str(len(occurrences)) + " occurrences of " + events[i] )
        plt.broken_barh(occurrences[x], (i*10,10), facecolors=(clrs[i % len(clrs)]))

    plt.savefig("out/" + filename + "_ganttchart.svg", bbox_inches='tight')
    


# Draw multiple trials with each trial on its own axis
# xmax set to 9 minutes (540 seconds)
# x = (x_start, x_len)
# y = Event name
def draw_group(dfs, trials, groupname=None, x="Bar", y="Event", xmax=540, sort=True):
    
    print("Drawing Gantt Chart...")
    
    # Declaring figure and its aspect ratio
    plt.figure(figsize=(20,8))
    
    # Find and sort unique Events alphabetically
    events = list(set(dfs[0][y]))
    if sort:
        events.sort()
     
    # Set limits
    plt.ylim(0, len(trials)*10)
    plt.xlim(0, xmax)
     
    # Setting axis labels
    plt.xlabel('Time (s)')
     
    # Setting ticks on y-axis
    plt.yticks([ (i*10)+ 5 for i in range(len(trials))], trials)
    
    # Setting ticks on x-axis
    plt.xticks(range(0,xmax+1,60))
    
    # Declare bars in chart
    for t in range(len(trials)):
        
        print('\n\t Trial ' + str(trials[t]) + '...')
            
        for e in range(len(events)):
            
            # Get all occurrences of the event and draw its bars
            occurrences = dfs[t][dfs[t][y] == events[e]]
            print("\t- Found " + str(len(occurrences)) + " occurrences of " + events[e] )
            plt.broken_barh(occurrences[x], (t*10,10), facecolors=(clrs[e % len(clrs)]))
        
        print()

    # Save plot
    name = "out/" 
    if groupname == None:
        name = name + "trials" + trials[0] + "-" + trials[-1]
    else:
        name = name + groupname 
        
    plt.savefig(name + "_ganttchart.svg", bbox_inches='tight')
    
    
    