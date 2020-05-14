import random 
import numpy as np 

### Random walker
##### Object Oriented Approach
class RandomWalker:
    def __init__(self):
        self.position = 0 
    
    def walk(self, n):
        self.position = 0 
        for i in range(n):
            yield self.position
            self.position += 2 * random.randint(0,1) - 1

    def get_position(self):
        return self.position


walker = RandomWalker()
walk = [position for position in walker.walk(1000)]

#10 loops, best of 3: 15.7 msec per loop

###### Procedural approach
def random_walk(n):
    position = 0 
    walk = [position]
    for i in range(n):
        position += 2*random.randint(0,1) - 1
        walk.append(position)
    return walk

walk = random_walk(1000)

#10 loops, best of 3: 15.6 msec per loop

##### Vectorized approach
def random_walk_faster(n=1000):
    from itertools import accumulate
    #only available from Python 3.6
    steps = random.choices([1,-1], k=n)
    return [0] + list(accumulate(steps))

# In fact, we've just vectorized our function. Instead of looping for picking sequential steps and add them to the current position, we first generated all the steps at once and used the accumulate function to compute all the positions. 
# We got rid of the loop and this makes things faster:

# 10 loops, best of 3: 2.21 msec per loop
# 
def random_walk_fastest(n=1000):
    steps = np.random.choice([-1,1], n)
    return np.cumsum(steps)

walk = random_walk_fastest(1000)
#1000 loops, best of 3: 14 usec per loop

