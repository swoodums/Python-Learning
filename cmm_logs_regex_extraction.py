# -*- coding: utf-8 -*-
"""
Created on Tue Jan 31 14:14:35 2023

@author: sam.woodbeck
"""
#This code is used to extract the sales line IDs from the CMM log files generated by the PIInspect app.  Lots of hard-coding and exceptions, but it's only the second bit of code I've written in Python.

#%% Import module and set up variables
import re
filename = 'RMT_CMM_2 - 2023-1.log'  #hard-coded.  Need to find a way to run through every log file in the directory.
pattern = '((563)\d{7})'  #RegEx pattern that searches for any 10-digit strings that begin with '563'.
new_file = []  #creates blank file to hold matches
#RSMT_CMM2_log = [] #creates log file.  Only needed for first run.  Need to find a way to create this once, then just append during the program run.

#%% Open the log into Python
with open(filename, 'r') as f:
    #Read the file contents and generate a list with each line
    lines = f.readlines()

#%% Iterate each line
for line in lines:
    #RegEx applied to each line
    match = re.search(pattern, line)
    if match:
        #Make sure to add \n to display correctly when we write it back
        new_line = match.group() + ' Jan 2023' + '\n' #hard coded based on filename.  Need to find a way to iterate this based on file name from PIInspect app.
        new_file.append(new_line)  #appends matches to file
        
#with open('RSMT_CMM2_log.txt', 'w') as f:
    #go to start of file
#    f.seek(0)
    #actually write the lines
#    f.writelines(new_file)
    
with open('RSMT_CMM2_log.txt', 'a') as f:  #opens file in append mode rather than write mode.
    f.writelines(new_file)  #appends lines