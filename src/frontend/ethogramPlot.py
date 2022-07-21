# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 12:50:49 2022

@author: Zahra Ghavasieh

Ethogram Plot
"""


import matplotlib
matplotlib.use('QtAgg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg

from model.ProjectModel import Project



class EthogramPlot(FigureCanvasQTAgg):
    
    def __init__(self, parent=None):
        
        self.fig = plt.figure(figsize=(12,8), dpi=100)
        self.axes = self.fig.add_subplot(111)
        super(EthogramPlot, self).__init__(self.fig)
        
        

    def drawPlot(self, proj:Project, xmax=None):
        
        if xmax == None:
            xmax = 0
            for b in proj.behaviours:
                maximum = max([e.start + e.length for e in b.events])
                xmax = max([xmax, maximum])
                    
         
        # Set limits
        plt.ylim(0, len(proj.behaviours)*10)
        plt.xlim(0, xmax)
         
        # Setting axis labels
        plt.xlabel('Time (s)')
         
        # Setting ticks on y-axis
        plt.yticks([ (i*10)+5 for i in range(len(proj.behaviours))], [b.name for b in proj.behaviours])
    
    
        # Setting ticks on x-axis
        plt.xticks(range(0, xmax+1, xmax // 5))
    
         
        # Setting graph attribute
        #plt.grid(True,axis='x')
        
        # Declare bars in chart
        for i in range(len(proj.behaviours)):
            
            # Get all occurrences of the event and draw its bars
            occurrences = proj.behaviours[i].events
            print("\t- Found " + str(len(occurrences)) + " occurrences of " + proj.behaviours[i].name ) #TODO remove
            broken_bars = [(e.start, e.length) for e in occurrences]
            plt.broken_barh(broken_bars, (i*10,10), facecolors=(proj.behaviours[i].colour))
    
        #plt.savefig("out/" + filename + "_ganttchart.svg", bbox_inches='tight')
        plt.close(self.fig)
    