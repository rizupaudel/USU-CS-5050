# open a gap score = openScore
# continue gap score = continueScore
# substitue score dictionary S
def align(n, m):
  if n == 0 and m == 0:
    return 0
  if n == 0:
    return openScore + continueDeleteB(0, m-1)
  if m == 0:
    return openScore + continueDeleteA(n-1, 0)
  return max(openScore + continueDeleteB(n, m-1),
             openScore + continueDeleteA(n-1, m),
             S[A[n], B[m]] + align(n-1, m-1))

def continueDeleteA(n, m):
  if n == 0:
    return align(n, m)
  return max(continueScore + continueDeleteA(n-1, m), align(n, m))

def continueDeleteB(n, m):
  if m == 0:
    return align(n, m)
  return max(continueScore + continueDeleteB(n-1, m), align(n, m))