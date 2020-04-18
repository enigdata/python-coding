#The serialization process is a way to convert a data structure into a linear form that can be stored or transmitted over a network
#The pickle module differs from the json module in that it serializes objects in a binary format, which means the result if not human readable.

import pickle

class example_class:
    a_number = 35
    a_string = 'hey'
    a_list = [1, 2, 3]
    a_dict = {'1': 'time', '2': 'happy', '3': 'strong'}
    a_tuple = (22, 23)

obj = example_class()

pickled_obj = pickle.dumps(obj)
print(f"This is my pickled object: \n{pickled_obj}\n")

unpickled_obj = pickle.loads(pickled_obj)
print(f"This is a_dict of the unpickled object:\n{unpickled_obj.a_dict}\n")

#Not everythig can ben pickled 
import dill 

square = lambda x: x * x 
my_pickle = dill.dumps(square)
#print(my_pickle)

#dill can serialize an entire interpreter session 
# square = lambda x: x * x
# a = square(35)
# import math 
# b = math.sqrt(484)
# import dill 
# dill.dump_session('test.pkl')
# exit()

# globals().items() 
# import dill 
# dill.load_session('test.pkl')
# globals().items()

#Customize pickling 
class foobar:
    def __init__(self):
        self.a = 35
        self.b = "test"
        self.c = lambda x: x * x 

    def __getstate__(self):
        attributes = self.__dict__.copy()
        del attributes['c']
        return attributes 

my_foobar = foobar()
my_pickle_string = pickle.dumps(my_foobar)
my_new_instance = pickle.loads(my_pickle_string)

print(my_new_instance.__dict__)

# To address this issue, you specify what to pickle with __getstate__(). You first clone the entire __dict__ of the instance to have all the attributes defined in the class, and then you manually remove the unpicklable c attribute.
# If you run this example and then deserialize the object, then you’ll see that the new instance doesn’t contain the c attribute

# But what if you wanted to do some additional initializations while unpickling, say by adding the excluded c object back to the deserialized instance? You can accomplish this with __setstate__():

class foobar2:
    def __init__(self):
        self.a = 35
        self.b = "test"
        self.c = lambda x: x * x 

    def __getstate__(self):
        attributes = self.__dict__.copy()
        del attributes['c']
        return attributes

    def __setstate__(self, state):
        self.__dict__ = state 
        self.c = lambda x: x * x 

another_foobar = foobar2()
another_pickle_string = pickle.dumps(another_foobar)
another_new_instance = pickle.loads(another_pickle_string)
print(another_new_instance.__dict__)


#Compression of Pickled Objects
import bz2 

my_string = """Per me si va ne la città dolente,
... per me si va ne l'etterno dolore,
... per me si va tra la perduta gente.
... Giustizia mosse il mio alto fattore:
... fecemi la divina podestate,
... la somma sapienza e 'l primo amore;
... dinanzi a me non fuor cose create
... se non etterne, e io etterno duro.
... Lasciate ogne speranza, voi ch'intrate."""

pickled = pickle.dumps(my_string)
compressed = bz2.compress(pickled)
print(len(my_string))
print(len(compressed))

#When using compression, bear in mind that smaller files come at a cost of a slower process 
#never unpickle data that comes from an untrusted source or is transmitted over an insecure network


