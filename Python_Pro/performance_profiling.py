### Profiling Tools

from timeit import timeit

setup = 'from datetime import datetime'
statement = 'datetime.now()'
result = timeit(setup=setup, stmt=statement)
print(f"Took an average of {result} ms")

#### CPU Profiling

# The cProfile module prints a few pieces of information about each method or function
# called while executing your program. For each call, it will show you
#  The number of times the call occurred (ncalls)
#  The time spent in that call alone, not including things it calls in turn (tottime)
#  The average time spent in that call alone, across the ncalls times it was called
# (percall)
#  The cumulative time spent in that call, including any time spent in subcalls
# (cumtime)

import random 
import time 

def an_expensive_function():
    execution_time = random.random() / 100
    time.sleep(execution_time)

if __name__ = "__main__":
    for _ in range(1000):
        an_expensive_function()

# Save this program in a cpu_profiling.py module. Then you can profile it from the
# command line using cProfile:

python3 -m cProfile --sort cumtime cpu_profiling.py

# When looking at the output of cProfile, you’ll want to search for calls with a high
# percall value or a big jump in cumtime. These characteristics mean the call takes up a
# good chunk of your program’s execution time. Speeding up a slow function can
# improve the program speed a fair amount, and cutting the execution time of a function
# that’s called thousands of times can be a really big win.