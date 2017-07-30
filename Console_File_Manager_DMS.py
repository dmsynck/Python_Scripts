#!/usr/bin/env python3

# Filename: Console_File_Manager_DMS.py

"""Purpose: This Python script implements the basic file / directory handling features
that a user would expect in a file manager type application. I didn't code the base
functionality (found on the web). However, I hope to extend it with my own feature
additions. Originally posted to the website www.codegeek.io by Nabarun Roy (July 2016)"""

# todo list for new functionality

# File / directory compare - not implemented yet
# File archiving operations - not implemented yet
# Disk usage statistics - not implemented yet

# Changelog

# 7/23/2017 - 

# Menu item #5 does not appear to work correctly. Need to check on this one.

# Menu item #6 partially fixed. Will find an existing directory, but not an existing file. Returns "file not found". Update - #6 seems to be fixed now.
# Will need more testing.

# 7/24/2017 -

# Menu item #5 fixed and tested. Needs paging for long output (using either OS 'more' or 'less' or Python 'subprocess' or 'Popen') into this function.

# Menu item # 6 fixed and tested.

# 7/26/2017 - 

# Worked on implementing file / directory compare

# File compare is working. Directory compare still not functional yet.

# First, we should import some needed modules.

import shutil     # Contains functions for working with files / directories, etc
import os         # Contains OS related functions
import subprocess
import filecmp

def Read():       # For reading files

    pathname = input("Enter the file location: (as an absolute path) \n")
    filename = input("Enter the file name: \n")
    target = os.path.join(pathname, filename)
    file = open(target,"r")
    print(file.read())
    input("Press 'Enter' to continue ... \n")
    file.close()

    return None

def Write():    # For writing or creating files

    pathname = input("Enter the file location: (as an absolute path) \n")
    filename = input("Enter the file name: \n")
    target = os.path.join(pathname, filename)

    if os.path.isfile(target):
        print("Overwriting existing file \n") # For existing file
    else:
        print("Creating new file \n") # For new file

    text = input("Enter the text to write: \n")
    file = open(target,"w")
    file.write(text)

    return None

def Add():      # Adding text to a file

    pathname = input("Enter the file location: (as an absolute path) \n")
    filename = input("Enter the file name: \n")
    target = os.path.join(pathname, filename)
    text = input("Enter the text to write: \n")
    file = open(target,"a")
    file.write('\n'+ text)

    return None

def Delete():          #Deleting a File

    pathname = input("Enter the file location: (as an absolute path) \n")
    filename = input("Enter the file name: \n")
    target = os.path.join(pathname, filename)

    if os.path.exists(target):      # checks if the file exists
        print("File Found \n")     # For existing file
        os.remove(target)          # os.remove(file path) is used to delete
        print("File has been deleted \n")
    else:
        print("File Does\'nt exist \n")    # If no file exists

    input("Press 'Enter' to continue ... \n")

    return None

def Dirlist():      # Listing files in a directory

    pathname = input("Enter the directory location to list: (as an absolute path) \n")
    sortlist = sorted(os.listdir(pathname))       # Sorting and listing files
    sortlist = subprocess.run(['ls -l | more'], stdout=subprocess.PIPE)

    print(sortlist.stdout)

    input("Press 'Enter' to continue ... \n")

    return None

def Check():       #Checking file or directory presence

    fp = int(input("Check the presence of \n 1.File \n 2.Directory \n"))

    if fp == 1:
        pathname = input("Enter the file location: (as an absolute path) \n")
        filename = input("Enter the file name: \n")
        target = os.path.join(pathname, filename)
        if os.path.isfile(target) == True:
            print("File Found \n")
        else:
            print("File not Found \n")
        input("Press 'Enter' to Continue ... \n")
    elif fp == 2:
        pathname = input("Enter the file location: (as an absolute path) \n")
        if os.path.isdir(pathname) == True:
            print("Directory Found \n")
        else:
            print("Directory Not Found \n")
        input("Press 'Enter' to Continue ... \n")
    else:
        pass

    return None

def Move():        # For moving or renameing file

    mr = int(input("1.Rename a file \n2.Move a file \n"))
    pathname_1 = input("Enter the current file location: (as an absolute path) \n")
    filename_1 = input("Enter the current file name: \n")
    target_1 = os.path.join(pathname_1, filename_1)

    if mr == 1:
        pathname_2 = input("Enter the destination path: (as an absolute path) \n")
        filename_2 = input("Enter the new file name: \n")
        target_2 = os.path.join(pathname_2, filename_2)
        shutil.move(target_1, target_2)
        print("File renamed \n")
    elif mr == 2:
        pathname_2 = input("Enter the destination path: (as an absolute path) \n")
        shutil.move(target_1, pathname_2)
        print("File moved \n")
    else:
        pass

    input("Press 'Enter' to continue ... \n")

    return None

def Copy():       #For copying

    pathname_1 = input("Enter the current file location: (as an absolute path) \n")
    filename_1 = input("Enter the current file name: \n")
    target_1 = os.path.join(pathname_1, filename_1)

    pathname_2 = input("Enter the destination path: (as an absolute path) \n")

    shutil.copy(target_1, pathname_2)
    print("File copied \n")
    input("Press 'Enter' to continue ... \n")

    return None

def Makedir():            #For creating directory

    pathname_1 = input("Enter the path for the new directory: (as an absolute path) \n")
    dirname_1 = input("Enter the name for the new directory: \n")
    target_1 = os.path.join(pathname_1, dirname_1)

    os.makedirs(target_1)

    print("Directory Created \n")
    input("Press 'Enter' to continue ... \n")

    return None

def Removedir():             # For removing Directory

    choice = int(input("1.Delete a single directory \n2.Delete an entire directory tree \n3.Exit \n"))

    if choice == 1:
        pathname_1 = input("Enter the path for the directory to remove: (as an absolute path) \n")
        os.rmdir(pathname_1)
        print("Directory deleted \n")
    elif choice == 2:
        pathname_1 = input("Enter the path for the directory tree to remove: (as an absolute path) \n")
        shutil.rmtree(pathname_1)
        print("Directory tree deleted \n")
    elif choice == 3:
        exit()
    else:
        pass

    input("Press 'Enter' to continue ... \n")

    return None

def RunProg():

    pathname_1 = input("Enter the path to the program / file: (as an absolute path) \n")
    filename_1 = input("Enter the name of the program / file to open: \n")
    target_1 = os.path.join(pathname_1, filename_1)

    try:
        subprocess.run(target_1)
    except:
        print("File not found \n")

    return None

def FileDirComp():

    choice = int(input("Would you like to compare: \n 1.Files \n 2.Directories \n"))

    if choice == 1:
        print("Enter information for the first file \n")
        pathname_1 = input("Enter the file location: (as an absolute path) \n")
        filename_1 = input("Enter the file name: \n")
        target_1 = os.path.join(pathname_1, filename_1)

        print("Enter information for the second file \n")
        pathname_2 = input("Enter the file location: (as an absolute path) \n")
        filename_2 = input("Enter the file name: \n")
        target_2 = os.path.join(pathname_2, filename_2)

        result = filecmp.cmp(target_1, target_2)

        if result == True:
            print("Files are equal \n")
        else:
            print("Files are not equal \n")
    elif choice == 2:
        pathname_1 = input("Enter the location for the first directory: (as an absolute path) \n")
        pathname_2 = input("Enter the location for the second directory: (as an absolute path) \n")

        result = filecmp.cmpfiles(pathname_1, pathname_2)

        for x in result:
            print(x)
    else:
        pass

    return None

def Run_Again():

    run = 0
    run = int(input("1.Run again \n\n2.Exit \n\nChoose the option number: \n\n"))

    if run == 1:
        Main()
    elif run == 2:
        exit()
    else:
        pass

    return None

def Main():

    run = 1

    while(run == 1):     #Running the program again

        os.system('clear')        #Used to clear the screen after running again the program
        print('DMS File Manager')

        dec = int(input('''
        1.Read a file
        2.Write to a file / Creata a new file
        3.Append to a file
        4.Delete a file
        5.List files in a directory
        6.Check if directory / file exists
        7.Move or rename a file
        8.Copy a file
        9.Create a directory
        10.Delete a directory / directory tree
        11.Run / open a program
        12.Compare files / directories
        15.Exit

        Choose the option number:'''))

        if dec == 1:
            Read()
            Run_Again()
        elif dec == 2:
            Write()
            Run_Again()
        elif dec == 3:
            Add()
            Run_Again()
        elif dec == 4:
            Delete()
            Run_Again()
        elif dec == 5:
            Dirlist()
            Run_Again()
        elif dec == 6:
            Check()
            Run_Again()
        elif dec == 7:
            Move()
            Run_Again()
        elif dec == 8:
            Copy()
            Run_Again()
        elif dec == 9:
            Makedir()
            Run_Again()
        elif dec == 10:
            Removedir()
            Run_Again()
        elif dec == 11:
            RunProg()
            Run_Again()
        elif dec == 12:
            FileDirComp()
            Run_Again()
        elif dec == 15:
            exit()
        else:
            pass
        exit()

    return None

Main()
