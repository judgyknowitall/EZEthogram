# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 16:44:42 2022

Author: Adam Lognon
@author: rlogn

Conda environment used: 
    conda activate C:/Users/rlogn/anaconda3/envs/APL-PyimageJ

File location:
    cd C:/Users/rlogn/Desktop/Adam-MSc-Files/Programming-practice

Script goal:
"""

import os
import tkinter as tk
from tkinter import Tk, filedialog
import time
import pandas as pd
import numpy as np
import win32com.client
import matplotlib.pyplot as plt
import matplotlib as mpl


# =============================================================================
# import csv
# from openpyxl import load_workbook
# =============================================================================


# Class object to keep the entire process within a self contained instance that has variables that are shared 
# between the functions via self. 
class app_start():
        
        #Initializes an instance of the app
        def __init__(self):
            super().__init__()
            
            self.run_app()
            
        #Choose the file for analysis 
        def select_file(self, query="Open Cleversys time bin excel sheet"):
            tk.Tk().withdraw()
            filetypes = [("Excel files","*.xlsx"),("CSV files", "*.csv"),("All files", "*.*")]
            self.fp = tk.filedialog.askopenfilename(title=query, filetypes=filetypes)
            if self.fp == '':
                quit()
            self.basepath = os.path.abspath(self.fp)
            self.fn, self.fe = os.path.splitext(self.fp)
            print(self.basepath)
            return self.fp, self.basepath, self.fe
        
# =============================================================================
#         # Function to save each excel worksheet as a seperate csv for analysis
#         # Based heavily on https://gist.github.com/julianthome/2d8546e7bed869079ab0f409ae0faa87
#         def sheets_to_csv(self, xlsx_file):
#             csvnames = []
#             csv_file = xlsx_file.replace('.xlsx','')
#             workbook = load_workbook(xlsx_file, data_only=True)
#             for sheets in workbook.get_sheet_names():
#                 try: 
#                     worksheet = workbook.get_sheet_by_name(sheets)
#                     print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#                     print(type(worksheet))
#                     print(worksheet)
#                     print('--------------------------------------------------------------------------------------------------------')
#                     csv_file = open(''.join([csv_file,'_',sheets,'.csv']), 'wb')
#                     wr = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
#                     for row in worksheet.iter_rows():
#                         lrow = []
#                         for cell in row:
#                             lrow.append(cell.value)
#                         wr.writerow(lrow)
#                     csvnames.append(''.join([csv_file,'_',sheets,'.csv']))
#                 except KeyError:
#                     print("The worksheet {} could not be found in the workbook".format(sheets))
#             return csvnames
# =============================================================================
        

        # Takes a single events file with 1 or more seperate trial sheets and converts
        # each sheet to an individual csv file
        def convertXLS2CSV(self, aFile):
            '''converts a MS Excel file to csv w/ the same name in the same directory'''
            
# =============================================================================
#             try:
# =============================================================================
            print ("------ beginning to convert XLS to CSV ------")
            csvnames = []

            excel = win32com.client.Dispatch('Excel.Application')
            excel.visible = False

            fileDir, fileName = os.path.split(aFile)
            workbook = excel.Workbooks.Open(aFile)
            nameOnly = os.path.splitext(fileName)
            
            newName = nameOnly[0] + ".csv"
            outCSV = os.path.join(fileDir, newName)
            newOutCSV = outCSV.replace("/", "\\")
            for sh in workbook.Sheets:
                #newcsv = excel.Workbooks.Add()
                sh.Copy()
                it1 = int(0)
                for wbs in excel.Workbooks:
                    if it1 > 0:
                        newOutCSV2 = newOutCSV.replace(".csv","_{}.csv".format(sh.Name))
                        wbs.SaveAs(newOutCSV2, 6)
                        wbs.Close(False)
                    it1 += 1
                csvnames.append(newOutCSV2)
                
            workbook.Close(False)
            excel.Quit()
            del excel

            print ("...Converted " + nameOnly[0] + " to CSV")
                
            return csvnames
# =============================================================================
#             except:
#                 print("\n")
#                 print("Sorry, file could not be found. Please try again")
#                 print("\n")
#                 self.select_file()
# =============================================================================
        
        # Changes dataframe headers to numbers
        def set_pd_head_num(self, dataframe): 
            it = 0
            newcol = []
            for cl in dataframe.columns:
                newcol.append(str(it))
                it += 1
            dataframe.columns = newcol
            dataframe.reset_index()
        
        # Takes a csv file for use by the program, will take the TopScan info and then prepare a 
        # dataframe with different sets of events. The required inputs are the filepath to an event csv
        # and an option for events to pull out, which by default will take all of the unique events
        # in the given csv file presented in the order that each event first occurs. 
        # The other eventset options have a maintained order and will present an event in the ethogram
        # even if the animal did not display that behaviour. Great for comparisons. 
        # Data is automatically sent to the make_ethogram function to create and save ethograms
        def prep_df(self, filepath, eventset='default'):
            alleventset = ['master', 'loco', 'area', 'misc', 'lowmov', 'major']
            
            # Setsup the data frame index unless it has already been done, could add a function to delete
            # the original non-indexed csv file
            if filepath.find('_ind') < 0:
                self.df = pd.read_csv(filepath)
                print("File not indexed")
                self.set_pd_head_num(self.df)
                self.df.reset_index()
                fp2 = filepath.replace(".csv","_ind.csv")
                self.df.to_csv(fp2)
            else: 
                self.df = pd.read_csv(filepath, index_col=0)
            self.events = self.df.iloc[:,4].unique()
            allevents = []
            # The master set has all the events that Adam Lognon used for his open field test (OFT)
            masterevents = ['Area:Mouse 1 Center In Box', 'Area:Mouse 1 Center In Periphery', 'Area:Mouse 1 Center In Center 50', 'Area:Mouse 1 Center In Center',
                            'Mouse 1 In Place Activity in Area Box', 'Mouse 1 In Place Activity in Area Periphery', 'Mouse 1 In Place Activity in Area Center 50', 'Mouse 1 In Place Activity in Area Center',
                            'Mouse 1 has no movement in Area Box', 'Mouse 1 has no movement in Area Periphery', 'Mouse 1 has no movement in Area Center 50', 'Mouse 1 has no movement in Area Center',
                            'Mouse 1 Locomotion in Area Box', 'Mouse 1 Locomotion in Area Periphery', 'Mouse 1 Locomotion in Area Center 50', 'Mouse 1 Locomotion in Area Center',
                            'Mouse 1 moving speed faster than     20.00 mm/s', 'Mouse 1 moving speed faster than     30.00 mm/s', 'Mouse 1 moving speed faster than     40.00 mm/s',
                            'Mouse 1 Turn Around','Mouse 1 Flat-Back Approach in Area Box', 'Mouse 1 Grooming in Area Box']
            # Loco set: Locomotor related events in different areas, and events that look at animal speed
            locoevents = ['Mouse 1 Locomotion in Area Box', 'Mouse 1 Locomotion in Area Periphery', 'Mouse 1 Locomotion in Area Center 50', 'Mouse 1 Locomotion in Area Center',
            'Mouse 1 moving speed faster than     20.00 mm/s', 'Mouse 1 moving speed faster than     30.00 mm/s', 'Mouse 1 moving speed faster than     40.00 mm/s']
            # Area set: Animal position in different arena spaces
            areaevents = ['Area:Mouse 1 Center In Box', 'Area:Mouse 1 Center In Periphery', 'Area:Mouse 1 Center In Center 50', 'Area:Mouse 1 Center In Center']
            # Misc set: Other behaviours that are less locomotor or position based 
            miscevents = ['Mouse 1 Turn Around','Mouse 1 Flat-Back Approach in Area Box', 'Mouse 1 Grooming in Area Box']
            # Lowmov set: Position/movement behaviours that are non-locomotor
            lowmovevents = ['Mouse 1 In Place Activity in Area Box', 'Mouse 1 In Place Activity in Area Periphery', 'Mouse 1 In Place Activity in Area Center 50', 'Mouse 1 In Place Activity in Area Center',
            'Mouse 1 has no movement in Area Box', 'Mouse 1 has no movement in Area Periphery', 'Mouse 1 has no movement in Area Center 50', 'Mouse 1 has no movement in Area Center']
            # Major set: The most important overall behavioural output set for Adam Lognon's OFT data set
            majevents = ['Mouse 1 has no movement in Area Box','Mouse 1 In Place Activity in Area Box','Mouse 1 moving speed faster than     20.00 mm/s', 'Mouse 1 Locomotion in Area Box']
            # Removes the Event header and potential nan instances from the events list
            for event in self.events:
                if event != 'Event' and str(event) != 'nan':
                    allevents.append(event)
            # Uses the event 'Area:Mouse 1 Center In Box' to obtain the trial duration. This won't be reliable for all use cases
            # A manual and automatic function could be used to set the trial duration, automatic taking the last end timepoint
            # in the end event column (may not be the best if none of the events are still ongoing by the end duration of the trial)
            self.triallen = self.df.iloc[self.df.index[self.df.iloc[:,4]=='Area:Mouse 1 Center In Box'],3].values[0]
            self.ethodata = []
            # The 'all' setting will iterate through all of the listed eventsets. There is likely a better way to organize this
            # with a list or a matrix
            if eventset != 'all':
                if eventset == 'default':
                    allevents = allevents
                elif eventset == 'master':
                    allevents = masterevents
                elif eventset == 'loco':
                    allevents = locoevents
                elif eventset == 'area':
                    allevents = areaevents    
                elif eventset == 'misc':
                    allevents = miscevents
                elif eventset == 'lowmov':
                    allevents = lowmovevents
                elif eventset == 'major':
                    allevents = majevents
                for event in self.allevents:
                    eventlog=[]
                    # Currently only pulls the start and stop time for each event, could be setup to obtain
                    # other info, eg. Distance traveled, if it is provided
                    starttimes = self.df.iloc[self.df.index[self.df.iloc[:,4]==event],1].values
                    durations = self.df.iloc[self.df.index[self.df.iloc[:,4]==event],3].values 
                    it4 = int(0)
                    for sts in starttimes:
                        templog=[]
                        templog=[float(sts),float(durations[it4])]
                        eventlog.append(templog)
                        it4 += 1
                        
                    self.ethodata.append([event, eventlog])
                self.make_ethogram(self.ethodata, eventset, filepath)
            
            # This elif statement is for iteratively running through all of the eventsets, meaning that each
            # trial will receive 6 figures
            elif eventset == 'all':
                for sets in alleventset:
                    self.ethodata = []
                    if sets == 'master':
                        allevents = masterevents
                    elif sets == 'loco':
                        allevents = locoevents
                    elif sets == 'area':
                        allevents = areaevents    
                    elif sets == 'misc':
                        allevents = miscevents
                    elif sets == 'lowmov':
                        allevents = lowmovevents
                    elif sets == 'major':
                        allevents = majevents
                    for event in allevents:
                        eventlog=[]
                        starttimes = self.df.iloc[self.df.index[self.df.iloc[:,4]==event],1].values
                        durations = self.df.iloc[self.df.index[self.df.iloc[:,4]==event],3].values 
                        it4 = int(0)
                        for sts in starttimes:
                            templog=[]
                            templog=[float(sts),float(durations[it4])]
                            eventlog.append(templog)
                            it4 += 1
                            
                        self.ethodata.append([event, eventlog])
                    self.make_ethogram(self.ethodata, sets, filepath)
                    
                
        
        #Data needs to have all events of an event type with the start time and duration like this: (start,duration)
        def make_ethogram(self, data, eventset, filename):
            mpl.style.use('default')
            fig, ax = plt.subplots()
            # Used the trial length to give the height a ratio, this could 
            # backfire with short duration trials
            graphheight = int(float(self.triallen)/4)
            # The normheight is the height for the bars, based on the number of event types plus 1 for the stimulation bar
            normheight = int(graphheight/(len(data)+1))
            # An iterating integer that is used to set the y positions of the bars, and rotate through the default bar colours
            it2 = int(1)
            heights=[]
            labels=[]
            # A bar for Adam Lognon's stimulation protocol
            ax.broken_barh([(600, 60),(840,60),(1080,60),(1320,60),(1560,60)], (0,normheight), facecolors='C0')
            heights.append(int(float(normheight)/2))
            labels.append('Stimulation')
            for event_type in data:
                for event in event_type[1]:
                    fc = it2 % 10
                    ax.broken_barh([(int(event[0]),int(event[1]))], (it2*normheight, normheight), facecolors='C{}'.format(fc))
                labels.append(str(event_type[0]))
                heights.append(int((float(normheight)/2)+(normheight*it2)))
                it2 += 1  
            ax.set_ylim(0, graphheight)
            ax.set_xlim(0, float(self.triallen))
            ax.set_xlabel('Time (s)')
            ax.set_yticks(heights, labels=labels)
            # Matplotlib figures are saved to the same folder that the csv originated from
            figpath = filename.replace('.csv','_fulletho_{}.svg'.format(eventset))
            plt.savefig(figpath, bbox_inches='tight', pad_inches=float(0.25) ,format='svg', dpi=float(450))
            
            
        # Body of the app for running the overall program. Will take a file, convert it to CSV if in 
        # another format, and then prep the dataframe. 
        def run_app(self):
            fp, bp, fe = self.select_file()
            if fe != ".csv":
                fps = self.convertXLS2CSV(fp)
                for paths in fps:
                   self.prep_df(paths, eventset='all')
            else:
                self.prep_df(fp, eventset='all')

            

# Body: Runs the program
app = app_start()
quit()
