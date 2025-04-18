
def bubble_sort(matrix):
    """Sorts first row of matrix of basis of bubble sort"""

    L = matrix[0] 
    n = len(L)
    counter = 0
    keepsorting = True
    while keepsorting == True:
        keepsorting = False
        for j in range(n-1):
            if L[j] > L[j+1]:
                counter +=1 
                L[j], L[j+1] = L[j+1], L[j]
                keepsorting = True
    return(L, counter)

def insertion_sort(matrix):
    """Sorts second row of matrix on basis of insertion sort"""

    L = matrix[1]
    counter = 0
    n = len(L)
    for i in range(n):
        j = i
        while j > 0 and L[j-1] > L[j]:
            counter += 1
            L[j-1], L[j] = L[j], L[j-1]
            j -= 1 #Sorts on basis of sublist [0, j]
    return(L, counter)

def selection_sort(matrix):
    """Sorts third row of matrix on basis of selection sort"""

    L = matrix[2]
    n = len(L)
    counter = 0
    for i in range(n):
        min_idx = i
        for j in range(i, n):
            if L[j] < L[min_idx]: #checks to see what lowest value is
                min_idx = j
        if L[i] != L[min_idx]:
            counter += 1 #if min index switches, swap occurs, counter goes up
        L[i], L[min_idx] = L[min_idx], L[i] #example i is lowest index, and now consists of lowest value
    return(L, counter)


def merge(first_row, second_row, third_row):
    """
    Merges three sorted rows of the matrix into one sorted 1D list.
    
    Args:
        matrix (list of list of int): 2D list (matrix) where each row has 'n' elements and is sorted.
    
    Returns:
        list: A merged 1D list that contains all elements from the matrix in sorted order.
    """
    sorted_list = []
    i = j = k = 0
    n = len(first_row)  # Since each row has the same number of elements
    
    while i < n or j < n or k < n:
        # Compare elements in each row, making sure to stay within bounds
        smallest = float('inf')
        target_row = 0

        if i < n and first_row[i] < smallest:
            smallest = first_row[i]
            target_row = 1
        if j < n and second_row[j] < smallest:
            smallest = second_row[j]
            target_row= 2
        if k < n and third_row[k] < smallest:
            smallest = third_row[k]
            target_row = 3

        # Add the smallest element to the merged list and move the corresponding index forward
        if target_row == 1: 
            sorted_list.append(first_row[i])
            i += 1
        elif target_row == 2:
            sorted_list.append(second_row[j])
            j += 1
        elif target_row == 3:
            sorted_list.append(third_row[k])
            k += 1

    return sorted_list
