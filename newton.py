import matplotlib as plt
import math
import numpy as np
# Python timeit() is a method in Python library to measure the execution time taken by the given code snippet
import timeit

def f(x):
    return x**3 -2*x- 5

def df(x):
    return 3*x**2-2

x0=1;
tolerance =1e-6
max_iterations=100

# the python loop
i =1;

starttime = timeit.default_timer()

for i in range(max_iterations):
#     increment i
    i= i+1;
    
#     assigning return values of fuctions values to variables
    fx = f(x0)
    
    dfx = df(x0)
    
    x1 = x0 -fx/dfx
    if abs(f(x1))<tolerance:
        print(f"Root at x ={x1:.6f}")
        break
    else:
        x0=x1
print(f"Time Taken To Execute: {timeit.default_timer() - starttime:.7f}")
