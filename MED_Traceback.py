import numpy as np
import random, string

def med(n, m):
    if n == 0:
        return m
    if m == 0:
        return n
    return min(med(n-1,m) + 1, med(n, m-1) + 1, med(n-1, m-1) + (A[n] != B[m]))
    

def medDP(n, m):
    global Sols
    Sols = np.zeros(shape = (n+1, m+1))
    for i in range(0, n+1):
        Sols[i,0] = i
    for j in range(0, m+1):
        Sols[0,j] = j
    for i in range(1, n+1):
        for j in range(1, m+1):
            Sols[i,j] = min(Sols[i-1,j] + 1, Sols[i, j-1] + 1, Sols[i-1, j-1] + (A[i] != B[j]))
    print(A)
    print(B)
    print Sols[n, m]
    return Sols[n, m]
    
def traceBack(i, j):
    global Sols
    # nothing to match
    if i == 0 and j == 0:
        return [] 
    # delete from A
    if Sols[i,j] == Sols[i-1,j] + 1:
        return [A[i] + " = _"] + traceBack(i-1, j)
    # delete from B
    if Sols[i,j] == Sols[i, j-1] + 1:
        return ["_ = " + B[j]] + traceBack(i, j-1)
    # must be match case, solution based on characters
    if A[i] != B[j]:
        return [A[i] + "<->" + B[j]] + traceBack(i-1, j-1)
    return [A[i] + "===" + B[j]] + traceBack(i-1, j-1)
    






A = "_AACCB"
B = "_ACCD"
    
print(medDP(len(A)-1, len(B)-1))
print(list(reversed(traceBack(len(A)-1, len(B)-1))))

def randomword(length):
   letters = string.ascii_lowercase[0:4]
   return '_' + ''.join(random.choice(letters) for i in range(length))
   
A = randomword(5)
B = randomword(5)
print(medDP(len(A)-1, len(B)-1))
print(list(reversed(traceBack(len(A)-1, len(B)-1))))
