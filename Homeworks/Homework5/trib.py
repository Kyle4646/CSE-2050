
def trib(k):
    '''makes a new dictionary everytime trib is called to prevent user putting in their own wrong 
    dictionary'''
    return _trib(k, dict())

def _trib(k, solved):
    '''returns values of tribonacci values using a cache to make it O(n)'''

    if k in solved:
        return(solved[k])
    if k == 1:
        return(0)
    if k == 2:
        return(0)
    if k == 3:
        return(1)
    solved[k] = _trib(k-1, solved) + _trib(k-2, solved) + _trib(k-3, solved)
    return(solved[k])


