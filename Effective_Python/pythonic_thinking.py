##### Know the difference between bytes, str and unicode
def to_string(bytes_or_string):
    if isinstance(bytes_or_string, bytes):
        value = bytes_or_string.decode('utf-8')
    else:
        value = bytes_or_string
    return value #this is a string instance

def to_bytes(bytes_or_string):
    if isinstance(bytes_or_string, str):
        value = bytes_or_string.encode('utf-8')
    else:
        value = bytes_or_string
    return value #this is a bytes instance

# “In Python 3, bytes contains sequences of 8-bit values, str contains sequences of Unicode characters. bytes and str instances can’t be used together with operators (like > or +)”

# Excerpt From: Brett Slatkin. “Effective Python: 59 Specific Ways to Write Better Python.” Apple Books. 

# “If you want to read or write binary data to/from a file, always open the file using a binary mode (like 'rb' or 'wb')”

# Excerpt From: Brett Slatkin. “Effective Python: 59 Specific Ways to Write Better Python.” Apple Books. 

##### Write helper functions instead of complex expressions

# “The if/else expression provides a more readable alternative to using Boolean operators like or and and in expressions.”

# Excerpt From: Brett Slatkin. “Effective Python: 59 Specific Ways to Write Better Python.” Apple Books. 

###### Know how to slice sequences
a = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
a[:]      # ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

