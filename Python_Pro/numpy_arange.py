import numpy as np 
np.arange

np.arange(start=1, stop=10, step=1)

#return an array

np.arange(1, 10, 1)
np.arange(10, step=3) #starts at 0

np.arange(1.0, 10, 1)
#returns array of floats

np.arange(1.0, 10, 0.1)

#descending array
np.array(10, 1, -1)

#### Datatypes with arange 
x = np.arange(10)
x.dtype #int64
x.size 
x.itemsize #8 bytes
## for color values:
np.arange(1,10,dtype=np.int8)

###### Manipulation
x = np.arange(5)
type(x) #class numpy array

2 ** x 
x ** 2 

x / 3 
x + 10 

x = np.arange(-10, 10, 0.5)
np.abs(x)

np.sin(x)

x = np.arange(1, 10)
x.shape
x.reshape(3,3)

##### arange vs. range 
#range only works with integers
list(range(10))
#range give a generator object

#If you want to work with numbers on demand and concerned about memory, use range
#np.arange is good at number sequences


#### other functions
np.linspace(1, 100, num=33)
np.linspace(1, 100, num=33, endpoint=False)

np.logspace(1, 100, num=33, endpoint=False)
np.geomspace(1, 100, num=33, endpoint=False)

x = np.array([1,2,3,4])
y = np.array([1,2,3,4])
np.meshgrid(x,y)


#### summary
#It is often better than Python in-built range object for work that
#requires heavy manipulation of the resulting sequences

#But the in-built range can be better for looping, especially if early exits are possible
