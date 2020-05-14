#### Stack
#last in first out 
#Examples: control + Z; chrome browsing history

##### Implement stack 
class SimpleStack(): 
    def __init__(self): 
        self.l = list() 
    def push(self, item): 
        self.l.append(item) 
        print(f"Pushed {item} to the stack") 
    def pop(self): 
        return self.l.pop() 
    def __repr__(self): 
        return "Top -> " + " ".join(list(reversed([str(x) for x in self.l]))) + " <- Bottom"  
    def __len__(self): # This is necessary for the 'while stack' section below
        return len(self.l)
        
####List 
stack = []
stack.append(1)
stack.append(2)
stack.append(3)

stack.pop()
stack.pop()
stack.pop()

#not the fastest solution

from collections import deque 

stack = deque()
stack.append(1)
stack.append(2)
stack.append(3)

stack.pop()
stack.pop()
stack.pop()

###### Concurrency with Python Stack
##Thread safety
#list generally not thread-safe
#deque requires more clarity

###Use queue.LifoQueue
#slightly more overhead than deque
from queue import LifoQueue 
stack = LifoQueue()
stack.put(1)
stack.put(2)
stack.put(3)

stack.queue

stack.get()
stack.get()
stack.get()

stack.get_nowait()

