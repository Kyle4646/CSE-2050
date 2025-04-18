
def _solve_puzzle(L):

    return _solve_puzzle(L, idx=0, mem=set())


def solve_puzzle(L, idx = 0, mem = None): # Make sure to add input parameters here
    """Returns True(False) if a given board is (is not) solveable"""

    if mem is None:
        mem = set()

    if idx == len(L)-1:
        return(True)
    
    idx_cw = (idx+L[idx]) % len(L)
    idx_ccw = (idx-L[idx]) % len(L)
    
    if (idx_cw in mem) and (idx_ccw in mem):
        return False
        
    mem.add(idx_cw)
    mem.add(idx_ccw)

    if solve_puzzle(L, idx_cw, mem) or solve_puzzle(L, idx_ccw, mem):
        return(True)
    
    return(False)
    


