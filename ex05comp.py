# Takes two lists, a and b, and return another with common elements.
# List comprehension with randomic testing.

import random

def overlap(a, b):
    newlist = list(set([x for x in a if x in b]))
    return newlist

if __name__ == "__main__":
    a = random.sample(range(20), 13)
    b = random.sample(range(20), 14)
    print(a)
    print(b)
    print(overlap(a, b))
    input()