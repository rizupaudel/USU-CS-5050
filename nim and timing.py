# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import sys
import datetime

sys.setrecursionlimit(2**15)  # does not appear to work for me

##Calculates the time taken by each function call and generates graph
def showTime(function, sizes, init = None, fit = 'exponential'):
  # times a given function and displays the time as a function of problem size
  #function takes a single integer argument
  #runs the function with an input values taken from input array sizes
  #generates a graph of run time as a function of problem size
  # init, if provided, is a function that is called once before function is called
  # fit may be 'exponential' then the time as a function of problem size is assumed
  #     to of the form time = c * a^n and the function solves for c and a
  #     where a is the base of the exponential function and c is a multiplicative factor
  #     sizes should be arithmeticly increasing (such as [10, 11, 12, 13, 14, 15])
  # fit my be 'polynomial' then the time as a function of problem size is assumed
  #     to of the form time = c * n ^ b and the function solves for c and b 
  #     where b is the power of n (the degree of the polynomial) and c is a multiplicative factor
  #     sizes should be geometrically increasing (such as [64, 128, 256, 512, 1024])
    timeLine = []
    validSizes = []
    for n in sizes:
        startTime = datetime.datetime.now()
        if not init == None:
            init()
        function(n)
        endTime = datetime.datetime.now()
        time_diff = (endTime - startTime)
        elapsed = time_diff.total_seconds() * 1000
        if elapsed > 0: #sometimes the function is too fast and we get 0 time
          timeLine.append(elapsed)
          validSizes.append(n)
    ##Generating the plot between time taken by each function call with n as variable and n
    plt.plot(validSizes, timeLine, 'g')
    plt.xlabel("n")
    if fit == 'exponential':
        plt.yscale('log')
    if fit == 'polynomial':
        plt.yscale('log')
        plt.xscale('log')
    plt.ylabel("time in milliseconds")
    plt.rcParams["figure.figsize"] = [16,9]
    plt.show()
    if fit == 'exponential': #fit a straight line to n and log time
        slope, intercept, _, _, _ = stats.linregress([validSizes], [np.log(t) for t in timeLine])
        print("time = %.6f %.3f ^ n" % (np.exp(intercept), np.exp(slope)))
    elif fit == 'polynomial': # fit a straight line to log n and log time
        slope, intercept, _, _, _ = stats.linregress([np.log(v) for v in validSizes], [np.log(t) for t in timeLine])
        print("time = %.6f n ^ %.3f" % (np.exp(intercept), slope))

def winNim(n):
  # implements NIM game where you can take between 1 and 10 stones off (if available)
  # your turn to move with n stones on the table
  # returns True if the position is a win for you, False if it is a loss
  if n == 0:
    return False
  if n == 1:
    return True
  ans = True
  for i in range(1,min(n+1, 11)):
    ans = ans and winNim(n-i)
 #   if not ans:
 #     break
  return not ans

def winNimMemo(n):
  # MEMOIZING 
  # implements a NIM game where you can take between 1 and 10 stones (if available)
  # your turn to move with n stones on the table
  # returns True if the position is a win for you, False if it is a loss
  global Cache # use Cache. Must be global, must be first initialized as empty
  if n == 0:
    return False
  if n == 1:
    return True
  #check if we have solved this problem already, if so return the solution
  if n in Cache: 
    return Cache[n]
  # need to solve this problem the first time
  # use the same problem decomposition and solution construction step
  ans = True
  for i in range(1,min(n+1, 11)):
    ans = ans and winNimMemo(n-i)
  # store the answer in the cache and return it
  Cache[n] = not ans
  return Cache[n]

#sets up the cache
def initWinMemo():
  # sets up a cache for the memoizing algorithm
  global Cache
  Cache = {}
  
# Experiment with the simple recursive algorithm
# use a set of problems that arithmetically increase in size
# uncomment the next line to run the experiment
showTime(winNim, [i for i in range(10, 30, 2)], fit = 'exponential')

# Experiment with the memoizing algorithm
# Use a geometricly increasing set of values
# initialize the cache each time
# uncomment the next line to run this experiment
# note the biggest problem is kept small because of problems with Python's recursion limit
# showTime(winNimMemo, [2**i for i in range(3, 12, 1)], init = initWinMemo, fit = 'polynomial')