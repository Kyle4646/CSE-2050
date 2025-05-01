
def idx_left(L, idx, right):
    '''Finds left index if less than right bound'''

    left = 2 * idx + 1
    return left if left < right else None

def idx_right(L, idx, right):
    '''Finds right index if less than right bound'''

    right_idx = 2 * idx + 2
    return right_idx if right_idx < right else None

def idx_max_child(L, idx, right):
    '''Finds index of max child'''

    left = idx_left(L, idx, right)
    right_idx = idx_right(L, idx, right)
    if left is None and right_idx is None:
        return None
    if right_idx is None:
        return left
    if left is None:
        return right_idx
    return left if L[left] > L[right_idx] else right_idx

def swap(L, i, j):
    '''Swaps two values in list'''

    L[i], L[j] = L[j], L[i]

def downheap(L, idx, right):
    '''Dowmnheaps a value to sort it in right place'''

    child = idx_max_child(L, idx, right)
    if child is not None and L[child] > L[idx]:
        swap(L, idx, child)
        downheap(L, child, right)

def heapsort(L):
    '''Downheaps all but leaves to ensure list is properly sorted'''

    n = len(L)
    for i in reversed(range(n // 2)):
        downheap(L, i, n)

    for i in reversed(range(1, n)):
        swap(L, 0, i)
        downheap(L, 0, i)
