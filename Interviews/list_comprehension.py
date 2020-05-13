lst = [1,2,-5, -4]

def square(x):
    return x*x 

map(square, lst)
list(map(square, lst))

###List comprehension
[square(x) for x in lst]

def is_odd(x):
    return x%2 == 1

lst = [1,2,-5,4]

odds = [num for num in lst if is_odd(num)]

#### More examples
grid = [[0,0,0],
        [0,0,0]]

num_rows = 2 
num_columns = 3

grid = []
for _ in range(num_rows):
    curr_row = []
    for _ in range(num_columns):
        curr_row.append(0)
    grid.append(curr_row)

grid = [[0 for _ in range(num_columns)] for _ in range(num_rows)]

### useful built-in functions
lst = [1,2,-5,4]
#Find the number that has the max square value
res = max(lst, key = lambda x: x*x)

min(lst, key = lambda x: x*x)
any(lst)

any([False, False])

any([(lambda x: x%2 ==1)(num) for num in lst])

all([(lambda x: x%2 == 1)(num) for num in lst])

