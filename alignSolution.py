import numpy as np

def med(n, m):
  if n == 0 and m == 0:
    return 0
  if n == 0:
    return 1 + med(0, m-1)
  if m == 0:
    return 1 + med(n-1, 0)
  return min(1+ med(n-1, m), 1 + med(n, m-1), (A[n] != B[m]) + med(n-1, m-1))

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
             S[(A[n],B[m])] + align(n-1, m-1))

def continueDeleteA(n, m):
  if n == 0:
    return align(n, m) #openScore + continueDeleteB(0, m-1)
  return max(continueScore + continueDeleteA(n-1, m), align(n, m))

def continueDeleteB(n, m):
  if m == 0:
    return align(n, m) #openScore + continueDeleteA(n-1, 0)
  return max(continueScore + continueDeleteB(n, m-1), align(n, m))

def alignDP(n, m):
  # use a 3D array, 0 = align, 1 = continueA, 2 = continueB
  global align
  align = np.ones((3, n+1, m+1), dtype=np.int32) * -100000

  #fill in base cases

  align[0, 0, 0] = 0
  align[1, 0, 0] = 0
  align[2, 0, 0] = 0
  for i in range(1, n+1): #m == 0
    align[1, i, 0] = continueScore + align[1, i - 1, 0] #continueA
    align[0, i, 0] = openScore + align[1, i - 1, 0] #open then continueA
  for j in range(1, m+1): #n == 0
    align[2, 0, j] = continueScore + align[2, 0, j - 1] #continueB
    align[0, 0, j] = openScore + align[2, 0, j - 1] #open then continueB
  # print(align)
  for i in range(1, n+1):
    for j in range(1, m+1):
      # align case
      align[0, i, j] = max(openScore + align[2, i, j - 1],
                           openScore + align[1, i - 1, j],
                           S[(A[i], B[j])] + align[0, i - 1, j - 1])
      # continue delete in A
      align[1, i, j] = max(continueScore + align[1, i - 1, j], align[0, i, j])
      # continue delete in B
      align[2, i, j] = max(continueScore + align[2, i, j - 1], align[0, i, j])
  #print(align)
  return align[0, n, m]

def traceAlign(i, j):
  trace = []
  scores = []
  whichSol = 0 #start in alignment
  while not (i == 0 and j == 0):
    # if not trace == []:
    #   print(trace[-1])
    # print((i,j))
    if whichSol == 0: #in alignment, use the three cases
      if align[0, i, j] == openScore + align[2, 0, j - 1]:
         trace.append("_ < %s" % B[j]) #open a gap 
         scores.append(openScore)
         j += -1
         whichSol = 2 #continue in B
      elif align[0, i, j] == openScore + align[1, i - 1, j]:
         trace.append("%s > _" % A[i]) #open a gap
         scores.append(openScore)
         i += -1
         whichSol = 1 #continue in A
      else: # align the characters
         trace.append("%s = %s" % (A[i], B[j])) 
         scores.append(S[(A[i], B[j])])
         i += -1
         j += -1
    elif whichSol == 1: #continue a gap in A
       if align[1, i, j] == continueScore + align[1, i - 1, j]: #continue in A
         trace.append("%s = _" % A[i]) #continue a gap
         scores.append(continueScore)
         i += -1
       else: #move to align
          whichSol = 0
    elif whichSol == 2: # continue in B
       if align[2, i, j] == continueScore + align[2, i, j - 1]:#continue in B
         trace.append("_ = %s" % B[j]) #continue a gap
         scores.append(continueScore)
         j += -1
       else: #move to align
         whichSol = 0
  return trace, scores

def test(a, b):
  global A, B
  A, B = a, b
  n = len(A)-1
  m = len(B)-1
  rScore = align(n, m)
  dScore = alignDP(n, m)
  trace, scores = traceAlign(n, m)
  # print(align)
  print("R %5d, D %5d " % (rScore, dScore))
  for matchScore in zip(trace, scores):
    print("%s  %3d" % matchScore)



S = {}
S[('A', 'A')] = 1
S[('T', 'T')] = 1
S[('A', 'T')] = -5
S[('T', 'A')] = -5

openScore = -5
continueScore = -1

A ='_TTTTTTT'
B ='_AAAAAAAT'

test(A, B)