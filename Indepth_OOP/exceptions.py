### Raising an exception
class EvenOnly(list):
    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("Only integers can be added")
        if integer%2:
            raise ValueError("Only even numbers can be added")

        super().append(integer)

# When an exception is raised, it appears to stop program execution immediately.  Anly lines
# that were supposed to run after the exception is raised are not executed, unless the exception is dealt with

def no_return():
    print("I am about to raise an exception")
    raise Exception("This is always raised")
    print("This line will never execute")
    return "Will not be returned"

#### Handling exceptions
try:
    no_return()
except:
    print("I caught an exception")
print("excecuted after the exception")

def funny_division(divider):
    try:
        return 100/divider
    except ZeroDivisionError:
        return "Zero is not a good idea!"

import random 
some_exceptions = [ValueError, TypeError, IndexError, None]

try:
    choice = random.choice(some_exceptions)
    print("raising {}".format(choice))
    if choice:
        raise choice("An Error")
except ValueError:
    print("Caught a Value Error")
except TypeError:
    print("Caught a Type Error")
except Exception as e:
    print("Caught some other error: %s" % (e.__class__.__name__))

else:
    print("This code called if there is no exception")
finally:
    print("This cleanup code is always called")

# Define your own exceptions
class InvalidWithdrawal(Exception):
    pass 

raise InvalidWithdrawal("You don't have $50 in your account")

#### Inventory Example with docstrings 

class Inventory:
    def lock(self, item_type):
        '''
        Select the type of item that is going to be manipulated.
        This method will lock the item so nobody else can manipulate 
        the inventory until it is returned.  This prevents selling 
        the same item to two different customers.
        '''
        pass 

    def unlock(self, item_type):
        '''
        Relase the given type so that other customers can access it.
        '''
        pass 

    def purchase(self, item_type):
        '''
        If the item is locked, raise an exception.
        If the item_type does not exist, raise an exception.
        If the item is currently out of stock, raise an exception.
        If the item is available, substract one item and return the number of items left.
        '''
        pass 
    
