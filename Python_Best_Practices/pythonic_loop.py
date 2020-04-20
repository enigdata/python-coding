#just iterate over the container 
my_items = [1, 5, 6]
for item in my_items:
    print(item)

#enumerate 
for i, item in enumerate(my_items):
    print(i, item)

# Writing C-style loops in Python is considered unpythonic 
# Avoid managing loop indexes and stop conditions manually if possible
# Python's for-loops are really "for-each" loops that can iterate over items from a container or sequence directly