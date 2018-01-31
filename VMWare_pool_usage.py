#!/usr/bin/env python3

# Filename: VMWare_pool_usage.py
# Python script to parse / display VMWare pool usage during a certain date range,
# based on data from a CSV file

# To be able to read a csv formatted file, we first have to import the csv module
import csv

# Open / read the PoolsData CSV file and build the list of pools
with open('PoolsData.csv', 'r') as f:
    reader = csv.reader(f)
    pool_list = []
    
    for row in reader:
        if row[1] not in pool_list:
            pool_list.append(row[1])
        else:
            pass
        
    f.close()
        
    print(pool_list)
    print()
    
    i = 1
    j = 0

    for item in pool_list:
        print(str(i) + ': ' + pool_list[j])
        i = int(i) + 1
        j = j + 1

    pool_list_size = len(pool_list)
    print()
    print('There are ' + str(pool_list_size) + ' pools')

    # Get user input on which pool they want usage data on
    print()
    print('Please select a pool by number to view usage')
    pool_selected = input()
    choice = True
    
    while choice:
        if pool_selected == '':
            print('Please make a selection from the pool list')
            pool_selected = input()
        if int(pool_selected) < 1:
            print('That is an invalid choice. Please select from 1 to ' + str(pool_list_size))
            pool_selected = input()
        elif int(pool_selected) > int(pool_list_size):
            print('That is an invalid choice. Please select from 1 to ' + str(pool_list_size))
            pool_selected = input()
        else:
            choice = False
            
    print('You selected: ' + pool_list[int(pool_selected) - 1])
    print()

# Get and display pool usage data for selected pool
with open('PoolsData.csv', 'r') as f:
    reader = csv.reader(f)
    pool_usage_list = []
    pool_usage_total = 0
    
    for row in reader:
        if row[1] == pool_list[int(pool_selected) - 1]:
            if row[2] == '0':
                pass
            else:
                pool_usage_list.append(row)
                pool_usage_total = pool_usage_total + int(row[2])
        else:
            pass
    
    f.close()
    
    pool_usage_list.sort(reverse=True)
    
    for item in pool_usage_list:
        print(item)

    print()

    print(str(pool_list[int(pool_selected) - 1]) + ' had a total of ' + str(pool_usage_total) + ' connections ')

    
        
            
    

  
                
        
    
        
        
