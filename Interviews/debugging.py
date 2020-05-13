### Print or breakpoint to debug

def max(lst):
    #max_num = 0 
    max_num = -float('inf')
    for num in lst:
        print(num, max_num)
        if num > max_num:
            print('entered if statement')
            max_num = num 
    return max_num 

print(max([-1, -2, -4]))

### Use pdb
def max(lst):
    #max_num = 0 
    max_num = -float('inf')
    for num in lst:
        breakpoint()
        if num > max_num:
            max_num = num 
    return max_num 

#press n to enter the next line of code