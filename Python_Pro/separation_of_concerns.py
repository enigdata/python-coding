###Namespacing
def add_sales_tax(total, tax_rate):
    return total*tax_rate

##Global namespace
TAX_RATES_BY_STATE = {
    'MT': 1.06,
    #...
}

def add_sales_tax(total, state):
    return total*TAX_RATES_BY_STATE[state]

import time 
import datetime
now = time.time()
midnight = datetime.time()

##decomposition
# Functions extract named concepts from procedural code.  Clarity and separation 
# are the primary objectives of extraction; reuse is a secondary benefit


