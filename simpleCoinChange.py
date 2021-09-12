def minCoins(n, v):
    if n ==0:
        return 0
    if n < 0:
        return float('inf')

    best = float ('inf')

    for i in range(len(v)):
        best = min(best, 1 + minCoins(n - v[i], v))

    return best

v = [5, 7, 8, 9, 25, 49]
n = 63
print (minCoins(n,v))