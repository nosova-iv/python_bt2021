import numpy as np
x = [10, 100, 1000]

def function(x):
    a = np.exp(1/np.sin((x)+1))
    b = 5/4 + 1/x**15
    c = np.log(a/b) / np.log((x**2)+1)
    return c

print(function(x[0]))
print(function(x[1]))
print(function(x[2]))



