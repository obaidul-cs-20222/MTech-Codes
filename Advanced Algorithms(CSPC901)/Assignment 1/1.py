import random
import math

def selectkth(A, l, r, kwish):
    # Find the pseudomedian
    pmed = mom(A[l:r+1])

    # Find the index of the pseudomedian
    pmedi = l
    while A[pmedi] != pmed:
        pmedi += 1

    # Swap that entry with the final entry
    A[r], A[pmedi] = A[pmedi], A[r]

    # Partition on the final entry
    pivotindex = partition(A, l, r)

    if kwish < pivotindex + 1:
        return selectkth(A, l, pivotindex - 1, kwish)
    elif kwish > pivotindex + 1:
        return selectkth(A, pivotindex + 1, r, kwish)
    else:
        return A[pivotindex]

def partition(A, l, r):
    pivot = A[r]
    t = l
    for i in range(l, r):
        if A[i] <= pivot:
            A[t], A[i] = A[i], A[t]
            t += 1
    A[t], A[r] = A[r], A[t]
    return t

def mom(A):
    # Make a copy because we’re going to mess it up doing our grouped sorting
    AA = A[:]
    n = len(AA)
    mlist = []

    for i in range(0, int(math.ceil(float(n) / 5))):
        Li = 5 * i
        Ri = Li + 5
        if Ri > n:
            Ri = n
        AA[Li:Ri] = sorted(AA[Li:Ri])
        mlist.append(AA[Li + (Ri - Li - 1) // 2])

    if len(mlist) == 1:
        return mlist[0]

    s = selectkth(mlist, 0, len(mlist) - 1, (len(mlist) + 1) // 2)
    return s

# Generate a list of 20 unique random integers between 0 and 100
LIST = []
while len(LIST) < 10000:
    r = random.randint(0, 100)
    if r not in LIST:
        LIST.append(r)

print('Array:', LIST)

kwish = random.randint(1, len(LIST))
kth = selectkth(LIST, 0, len(LIST) - 1, kwish)

print("I'm looking for rank:", kwish)
print('It is:', kth)

# print('Here is the Python sorted array for checking:')
# LIST.sort()
# print(LIST)

if LIST[kwish - 1] == kth:
    print('Success!')