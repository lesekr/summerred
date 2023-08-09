#!/usr/bin/env python3.7

import os

#List of files in the working directory
directory = os.getcwd()

#Create a directory
directoryname = []

#Create an empty list to store the directories
filesdes = []

#Go over files in the working directory
for filename in os.listdir(directory):
    
    file_size = os.path.getsize(filename)
    modified_time = os.path.getmtime(filename)
    creation_time = os.path.getctime(filename)
    file_path = os.path.realpath(filename)
   
    #Inputting dictionary to the list
    filesdes.append({'name': filename, 'size': file_size, 'time': modified_time, 'path': file_path})

#Print Dictionary    
print (*filesdes,sep="\n")