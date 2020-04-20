# This is what I was trying to do here 

# This is a comment

#Docstring
"""Form a complex number.

Keyword arguments:
real -- the real part (default 0.0)
imag -- the imaginary part (default 0.0)
"""

def factorial(n: int) -> int:
    """Recursive factorial

    Recursively compute a factorial

    Arguments:
    n -- the integer to compute the factorial
    """
    if n == 2:
        return 2
    else:
        return n * factorial(n -1)

if __name__ == "__main__":
    print(factorial(5))


#bulk comment: highlight, then command + /

#DRY: Don't Repeat Yoursefl
#Do not write twice 