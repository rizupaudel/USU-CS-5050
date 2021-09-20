import numpy as np
from random import randint
import showTime

def maxValue(length):
    global Values
    if length == 0:
        return 0
    return max([maxValue(length - i) + Values[i]
                for i in range(1, min(length + 1, len(Values)))])
                
def memo(length):
    global Sols
    Sols = [-1]*(length + 1)
    maxValueMemo(length)
    return Sols[length]
    
def maxValueMemo(length):
    global Values
    if length == 0:
        return 0
    if Sols[length] > 0:
        return Sols[length]
    Sols[length] = max([maxValueMemo(length - i) + Values[i] 
                        for i in range(1, min(length + 1, len(Values)))])
    return Sols[length] 
                
def DPmaxValue(length):
    global Sols, Values
    # allocate memory, setup base case
    Sols = [0]*(length + 1)
    # all possible problem lengths
    for j in range(1, length+1):
        # length -- > j
        # solution construction from smaller sub solutions
        Sols[j] = max([Sols[j - i] + Values[i] 
                       for i in range(1, min(j + 1, len(Values)))])
    # return 
    return Sols[length]
    
def cutsR(length):
    # recursive
    global Sols, Values
    # nothing to cut
    if length == 0:
        return []
    # which subsolution was used for my solution?
    for i in range(1, min(length + 1, len(Values))):
        if Sols[length - i] + Values[i]  == Sols[length]:
            return [ i ] + cutsR(length - i)
    
def cuts(length):
    # iterative
    global Sols, Values
    cutLengths = []
    while length > 0:
        # which subsolution was used for my solution?
        for i in range(1, min(length + 1, len(Values))):
            if Sols[length - i] + Values[i] == Sols[length]:
                cutLengths.append(i)
                length = length - i
                break
    return cutLengths
    
Values = [0] + [randint(1, 2*i) for i in range(1, 20)]

# TIMING EXPERIMENTS
# RECURSIVE
#showTime.showTime(maxValue, [i for i in range(8, 22)], fit = 'exponential')
# DYNAMIC PROGRAMMING
#showTime.showTime(DPmaxValue, [2**i for i in range(6, 22)], fit = 'polynomial')

for i in range(100):
    primes = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71]
    
    length = primes[randint(0, 8)] #len(primes)-1)] #7+1)
    # best = DPmaxValue(length)
    # if not best == maxValue(length) or not best == memo(length):
    #     print("Bug")
    # print("Length = %d, Value = %d, cuts = %s" % (length, best, cuts(length)))
    
Values = [0,2,3,7]
L = 11
print(DPmaxValue(L))
cutList = cuts(L)
print("$%d %s" % (sum(Values[i] for i in cutList), cutList))
cutList = cutsR(L)
print("$%d %s" % (sum(Values[i] for i in cutList), cutList))
    

                       
    

                
