# Filename: Console_File_Manager_DMS.py

""" 
Purpose: This Python script implements the basic file / directory handling features
that a user would expect in a file manager type application. I didn't code the base
functionality (found on the web). However, I hope to extend it with my own feature
additions. Originally posted to the website www.codegeek.io by Nabarun Roy (July 2016)
"""

# Tested functionality

# Menu items #1, #2, #3, #4, and #12 have been tested and seem to function as expected

# Non-working functionality
# Menu item #5 and #6 don't seem to work quite correctly. Need to check further into these functions.

# todo list for new functionality

# File / directory compare - not implemented yet
# File archiving operations - not implemented yet
# Disk usage statistics - not implemented yet

# First, we should import some needed modules.

import shutil     # Contains functions for working with files / directories, etc
import os         # Contains OS related functions

def Read():       # For reading files

    path = input("Enter the location of file to read:")
    file = open(path,"r")
    print(file.read())
    input('Press Enter...')
    file.close()

    return None

def Write():    #For writing or creating files

    path = input("Enter the location of file to write or create:")
    if os.path.isfile(path):
        print('Rebuilding Existing file') #For existing file
    else:
        print('Creating new file') #For new file
    text = input("Enter the text to write:")
    file = open(path,"w")
    file.write(text)

    return None

def Add():      # Adding text to a file

    path = input("Enter the file location:")
    text = input("Enter the text to write:")
    file = open(path,"a")
    file.write('\n'+text)

    return None

def Delete():          #Deleting a File

    path = input("Enter the location of file to be write or create:")
    if os.path.exists(path):      # checks if the file exists
        print('File Found')     #For existing file
        os.remove(path)          #os.remove(file path) is used to delete
        print('File has been deleted')
    else:
        print('File Does\'nt exist')    #Is no file exist

    return None

def Dirlist():      #Listing files in a directory

    path = input("Enter the Directory location to list:")
    sortlist = sorted(os.listdir(path))       #Sorting and listing files
    i = 0
    while(i < len(sortlist)):
        print(sortlist[i] + '\n')
        i += 1

    return None

def Check():       #Checking file or directory presence

    fp = int(input('Check the presence of \n1.File \n2.Directry \n'))
    if fp == 1:
        path=input("Enter the file location:")
        os.path.isfile(path)
        if os.path.isfile(path) == True:
            print('File Found')
        else:
            print('File not Found')
    if fp == 2:
        path = input("Enter the Directory location:")
        os.path.isdir(path)
        if os.path.isdir(path) == False:
            print('Directory Found')
        else:
            print('Directory Not Found')

    return None

def Move():        #For moving or renameing file

    path1 = input('Enter the location of File to move or rename:')
    mr = int(input('1.Rename \n2.Move \n'))
    if mr == 1:
        path2 = input('Enter the resulting location with resulting file name:')
        shutil.move(path1, path2)
        print('File renamed')
    if mr == 2:
        path2 = input('Enter the location to move:')
        shutil.move(path1, path2)
        print('File moved')

    return None

def Copy():       #For copying

    path1 = input('Enter the location of File to copy or rename:')
    path2 = input('Enter the location to copy:')
    shutil.copy(path1, path2)
    print('File copied')

    return None

def Makedir():            #For creating directory

    path = input("Enter the directory name with location to make \neg. C:\\Hello\\Newdir \nWhere newdir is new directory:")
    os.makedirs(path)
    print('Directory Created')

    return None

def Removedir():             #For removing Directory

    path = input('Enter the location of Directory:')
    treedir = int(input('1.Deleted Directory \n2.Delete Directory Tree \n3.Exit \n'))
    if treedir == 1:
        os.rmdir(path)
    if treedir == 2:
        shutil.rmtree(path)
        print('Directory Deleted')
    if treedir == 3:
        exit()

    return None

def Openfile():

    path = input('Enter the location of Program:')
    try:
        os.startfile(path)
    except:
        print('File not found')

    return None

def Main():

    run = 1
    while(run == 1):     #Running the program again
        os.system('cls')        #Used to clear the screen after running again the program
        print('DMS File Manager')
        dec = int(input('''
                       1.Read a file
                       2.Write to / Creata a File
                       3.Append to a File
                       4.Delete a file
                       5.List files in a directory
                       6.Check file existence
                       7.Move a file
                       8.Copy a file
                       9.Create a directory
                       10.Delete A directory
                       11.Open a program
                       12.Exit
                       Choose the option number:'''))

        if dec == 1:
            Read()
        elif dec == 2:
            Write()
        elif dec == 3:
            Add()
        elif dec == 4:
            Delete()
        elif dec == 5:
            Dirlist()
        elif dec == 6:
            Check()
        elif dec == 7:
            Move()
        elif dec == 8:
            Copy()
        elif dec == 9:
            Makedir()
        elif dec == 10:
            Removedir()
        elif dec == 11:
            Openfile()
        elif dec == 12:
            exit()
        else:
            pass
    run = int(input("1.Run again \n2.Exit \nChoose the option number: \n"))
    if run == 2:
        exit()

    return None

Main()
