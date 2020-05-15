print(f'Invoking __init__.py for {__name__}')
__all__ = [
    'mod1',
    'mod2'
]

import pkg.mod1, pkg.mod2
#global variables
alist = ['spam', 'bacon', 'eggs']
