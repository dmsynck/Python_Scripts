# Python script to parse / display VDI pool usage during a certain date range, based on log data from a CSV file.
# 
# User can either select a particular pool or get usage data for all the pools

# To be able to read a csv formatted file, we first have to import the csv module
import csv

def get_User_Input():
    print("""Which task would you like to do: ? \n
             1. View usage for a particular pool \n
             2. View usage for all pools \n """)
             
    user_choice = input('Please enter the number of the task you want to perform \n \n')

    choice_loop = True

    while choice_loop:
        
        if user_choice == '1':
            print('You entered: ' + user_choice)
            choice_loop = False
            get_Usage_One_Pool()
        elif user_choice == '2':
            print('You entered: ' + user_choice)
            choice_loop = False
            get_Usage_All_Pools()
        else:
            print('That entry was invalid. Please try again')
            user_choice = input('Please enter the number of the task you want to perform \n \n')
    
def get_Usage_One_Pool():

    # Open / read the PoolsData CSV file and build the list of pools

    with open('PoolsData.csv', 'r') as f:
        reader = csv.reader(f)
        pool_list = []
        pool_list_size = 0
        pool_selected = ''
        pool_usage_list = []
        pool_usage_total = 0
        i = 1
        j = 0
        
        for row in reader:
            if row[1] not in pool_list:
                pool_list.append(row[1])
            else:
                pass
            
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
        choice_loop = True
        
        while choice_loop:
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
                choice_loop = False
                
        print('You selected: ' + pool_list[int(pool_selected) - 1] + ' \n')
        print()

        f.seek(0)

        for row in reader:
            if row[1] == pool_list[int(pool_selected) - 1]:
                if int(row[2]) == 0:
                    pass
                else:
                    pool_usage_list.append(row)
                    pool_usage_total = pool_usage_total + int(row[2])
            else:
                pass
        
        pool_usage_list.sort(reverse=True)
        
        for item in pool_usage_list:
            print(item)

        print()

        print(str(pool_list[int(pool_selected) - 1]) + ' had a total of ' + str(pool_usage_total) + ' connections')

        f.close()

def get_Usage_All_Pools():

    pool_list = []
    connections_counter = 0
    
    # Open / read the PoolsData CSV file and build the list of pools

    with open('PoolsData.csv', 'r') as f:
        reader = csv.reader(f)
        
        for row in reader:
            if row[1] not in pool_list:
                pool_list.append(row[1])
            else:
                pass

        f.seek(0)

        for item in pool_list:

            for row in reader:
                
                if item == row[1]:
                    connections_counter = connections_counter + int(row[2])
                else:
                    pass

            print(item +  ' Total # of Connections ' + str(connections_counter))

            connections_counter = 0

            f.seek(0)

# Script execution starts with a call to get_User_Input()

get_User_Input()

        
    
            
        

        
        
        
            
        
        
                
    
        
        


        
                    





    
        
            
    

  
                
        
    
        
        
