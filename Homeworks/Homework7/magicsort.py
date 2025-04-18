import math
from enum import Enum
import random

INVERSION_BOUND = 10  # pre-defined constant; independent of list input sizes

class MagicCase(Enum):
    """Enumeration for tracking which case we want to use in magicsort"""
    GENERAL = 0
    SORTED = 1
    CONSTANT_INVERSIONS = 2
    REVERSE_SORTED = 3

def linear_scan(L):
    '''Checks how many inversions are in a list'''
    
    counter = 0
    for i in range(len(L)-1):
        if L[i] > L[i+1]:
            counter += 1
    if counter == 0: return(MagicCase.SORTED)
    elif counter == (len(L)-1): return(MagicCase.REVERSE_SORTED) #reversed list if everyvalue's next is smaller
    elif counter <= INVERSION_BOUND: return(MagicCase.CONSTANT_INVERSIONS) #not a lot of swaps
    else: return(MagicCase.GENERAL)

def reverse_list(L, alg_set=None):
    '''Reverses a list in O(n)'''

    for i in range(len(L)//2):
        L[i], L[len(L) - 1 - i] = L[len(L) - 1 -i], L[i] #At most O(n//2), so O(n)
        #Also in-place, never makes new list

def magic_insertionsort(L, left, right, alg_set=None):
    '''Does an insertion sort, preferably for lists with few inversions'''
    
    for i in range(left, right):
        j = i
        while j > left and L[j-1] > L[j]:
            L[j-1], L[j] = L[j], L[j-1]
            j -= 1
    return()


def magic_mergesort(L, left, right, alg_set=None):
    '''Calls magic_mergesort if more than 20 items'''

    if alg_set is None:
        alg_set = set()
    
    if right - left < 20:
        alg_set.add('magic_insertionsort')
        magic_insertionsort(L, left, right, alg_set)
        return()
    median = (left + right) // 2
    magic_mergesort(L, left, median, alg_set)
    magic_mergesort(L, median, right, alg_set) 
    merge(L, left, median, right)
    return()

def merge(L, left, median, right):
    '''merges the lists'''

    A = L[left:median]
    B = L[median:right]
    i = j = 0
    k = left
    
    while (i < len(A)) and (j < len(B)):
        if A[i] < B[j]:
            L[k] = A[i]
            i += 1
        else: 
            L[k] = B[j]
            j += 1
        k += 1

    while i < len(A):
        L[k] = A[i]
        i += 1
        k += 1

    while j < len(B):
        L[k] = B[j]
        j += 1
        k += 1


def magic_quicksort(L, left, right, depth=0, alg_set=None):
    '''Calls quicksort for general cases'''

    if alg_set is None:
        alg_set = set()


    if right - left < 2:
        return()
    if (right-left) < 20:
        alg_set.add('magic_insertionsort')
        magic_insertionsort(L, left, right, alg_set)
        return()
    alg_set.add('magic_quicksort')
    pivot = _partition(L, left, right)
    if depth > 3:
        alg_set.add('magic_mergesort')
        magic_mergesort(L, left, right, alg_set)
        return()
    magic_quicksort(L, left, pivot, depth + 1, alg_set)
    magic_quicksort(L, pivot+1, right, depth + 1, alg_set)

def _partition(L, left, right):
    '''Splits list on basis of pivot'''
    pivot = right-1
    i = left
    j = pivot - 1
    while i <= j:
        while i <= j and L[i] < L[pivot]:
            i += 1
        while i <= j and (L[j] >= L[pivot]):
            j -= 1
        if i < j:
            L[i], L[j] = L[j], L[i]
   
    L[pivot], L[i] = L[i], L[pivot]
    pivot = i
    return(pivot)


def magicsort(L):
    '''Does the magicsort and makes it O(n) on basis of case'''

    alg_set = set()

    if linear_scan(L) == MagicCase.SORTED:
        return(alg_set) #O(1)
    elif linear_scan(L) == MagicCase.REVERSE_SORTED:
        reverse_list(L) #O(n)
        alg_set.add('reverse_list')
        return(alg_set)
    elif linear_scan(L) == MagicCase.CONSTANT_INVERSIONS:
        magic_insertionsort(L, 0, len(L)) #Fast, little items
        alg_set.add('magic_insertionsort')
        return(alg_set)
    elif linear_scan(L) == MagicCase.GENERAL:
        magic_quicksort(L, 0, len(L), alg_set = alg_set) #O(nlogn) since never runs for its worst cases
        return(alg_set)