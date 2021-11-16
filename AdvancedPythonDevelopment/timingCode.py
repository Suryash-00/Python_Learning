import time

def powers(limit):
    return [x**2 for x in range(limit)]

start= time.time()
powers(5000000)
end=time.time()
print(end-start)

import timeit

print(timeit.timeit("[x**2 for x in range(10)]"))