
import random
import time

def generate_lists(size):
    '''This generates lists of random integers using random function'''
    
    if (size >= 0):
        
        list1 = random.sample(range(size*2), size) #makes random list size of unique items. Has size items but ranges from 0 to 2*size.
        
        list2 = random.sample(range(size*2), size)
        
        return(list1, list2)


def find_common(list1, list2):
    '''Uses O(n^2) algorithm to see if items in a list are similar'''
    
    counter = 0 #2 operations, counter initialized and setting it to value
    
    for item in list1: #n times
        for newitem in list2: #n times, but this happens n times due to for loop above (n^2)
            if item == newitem: #cost 1 is but happens n^2 times
                counter += 1 #cost is 2 but can happen 2n^2
    
    return(counter) #1

    #total = 3n^2+3;  O(n^2)


def find_common_efficient(list1, list2):
    '''Uses O(n) algorithm to see how many similar items are in list.
    Acquires O(n) using sets, where sorting throgh is O(1) due to hasing'''
    
    counter = 0
    
    list2 = set(list2) #n goes through n items to make set
    
    for item in list1: #n
        if item in list2: #1 Checking to see if item in set is only 1 cost, but this can happen n times (n)
            counter += 1 #2n (4n)
    
    return(counter) #1

    #total = 4n+3; O(n)
    

def measure_time():
    '''Prints a table of items and times for the common list and common efficient
    list. '''
    
    time_list = [10, 100, 1000, 10000, 20000]
    generate_list_times = []
    generate_list_efficient_times = []

    for amount in time_list: #common_list
        start = time.time()
        find_common(*generate_lists(amount)) #uses star to take tuple of lists as sepeerate parameters          
        generate_list_times.append(time.time() - start)
    
    for amount in time_list: #common_list_efficency
        start = time.time()
        find_common_efficient(*generate_lists(amount))
        generate_list_efficient_times.append(time.time() - start)

    print(f'List Size:     find__common Times(s)      find_common_efficient Times(s)')
    print(f'----------     ---------------------      ------------------------------')
    
    for index, value in enumerate(time_list):
        print(f'{value}             {generate_list_times[index]:.15f}           {generate_list_efficient_times[index]}')


if __name__ == "__main__":
    measure_time()

   
   

    

