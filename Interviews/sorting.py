animals = ["cat", "dog", "cheetah", "rhino"]
sorted(animals) #returns a new list; animals list does not change
sorted(animals, reverse=True)

animals = [
    {'type': 'cat', 'name': 'Stephanie', 'age': 8},
    {'type': 'dog', 'name': 'Devon', 'age': 10},
    {'type': 'rhino', 'name': 'Bob', 'age': 3}
]

sorted(animals, key = lambda x: x['age'], reverse=True)

#change in place
animals.sort(key=lambda x: x['age'])

