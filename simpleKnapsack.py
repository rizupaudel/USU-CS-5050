###########################
from random import random, randint

N = 7
K = 100

def knapsackBool(i, size):
    if size == 0:
        return True
    if size < 0:
        return False
    if i == 0:
        return False
    return knapsackBool(i-1, size) or knapsackBool(i-1, size - S[i])
    
for _ in range(0,100):
    S = [randint(1,K/2) for _ in range(0,N + 1)]
    if knapsackBool(N, K):
        print("Solution exists")
    else:
        print("Solution does not exist")
        
    
    
N = 5
K = 10
S = [None, 11,12,23,435,44,4,20]
print(knapsackBool(N, K))
        
