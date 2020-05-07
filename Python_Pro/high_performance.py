### Understanding time and space complexity
### Measuring the complexity of your code
### Choosing data types for different activities in Python

################ Memory 

# In Python, you can read a file line-by-line in a for loop, and on each iteration of
# the loop, the next line will replace the current line in memory.

color_counts = {}

with open('all-favorite-colors.txt') as favorite_colors_file:
    for color in favorite_colors_file:
        color = color.strip()

        if color in color_counts:
            color_counts[color] += 1 
        else:
            color_counts[color] = 1 

#Space complexity is O(1)

# Many big web applications emit logs of their activity so they can be debugged or
# analyzed. If you introduce a log statement in your code that gets called 1,000 times
# per minute in production, this could start eating up disk space quickly. You might
# want to remove that line, move it somewhere that gets called less frequently, or
# improve your strategy for storing logs.

all_colors = set()
with open('all-favorite-colors.txt') as favorite_colors_file:
    for line in favorite_colors_file:
        all_colors.add(line.strip())

# Generators are constructs in Python that produce a single value at a
# time, pausing until the next value is requested (figure 4.5). This acts a lot like the
# approach you used earlier to read a file line-by-line. By yielding one value at a time, a
# generator avoids storing all values it produces in memory at once.

# yield works a lot like Python’s return statement, except that you can perform
# operations after you yield a value

## Using yield to pause and prepare:
def range(*args):
    if len(args) == 1:
        start = 0 
        stop = args[0]

    else:
        start = args[0]
        stop = args[1]

    current = start 
    while current < stop:
        yield current #yields each value one at a time
        current += 1 

## A short generator that yields squared numbers 
def squares(items):
    for item in items:
        yield item**2

# I recommend making use of generators over lists wherever you can, because you can
# always build a full list in memory from a generator if needed by writing
# list(range(10000)) or list(squares([1, 2, 3, 4])). Using generators will save
# memory, but it can also save time because the code consuming the values from the
# generator may not need them all anyway.

## Make it Work; Make it Right; Make it Fast

## Example:

def get_number_with_highest_count(counts):
    max_count = 0 
    for num, count in counts.items():
        if count > max_count:
            max_count = count
            res_number = num 

    return res_number

def most_frequent(numbers):
    counts = {}
    for num in numbers:
        if num in counts:
            counts[num] += 1 
        else:
            counts[num] = 1 

    return get_number_with_highest_count(counts)

#Improve: use defaultdict 
from collections import defaultdict

def most_frequent(numbers):
    counts = defaultdict(int)
    for num in numbers:
        counts[num] += 1 

    return get_number_with_highest_count(counts)

#Improve: use counter
from collections import Counter

def most_frequent(numbers):
    counts = Counter(numbers)
    return get_number_with_highest_count(counts)

#Improve more
def get_number_with_highest_count(counts):
    return max(counts, key = lambda x: counts[x])

def most_frequent(numbers):
    return get_number_with_highest_count(counts)


