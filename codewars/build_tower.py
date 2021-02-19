"""
Build Tower
Build Tower by the following given argument:
number of floors (integer and always greater than 0).

Tower block is represented as *

for example, a tower of 3 floors looks like below

[
  '  *  ', 
  ' *** ', 
  '*****'
]
"""

def tower_builder(n_floors):
    l = []
    for i in range(1, n_floors+1):
        l.append(
            ("*"*(2*i-1)).center(2*n_floors-1)
        )
    return l