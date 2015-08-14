# Common elements in two lists. No duplicates. 
import random

def overlap(a, b):
    newlist = list(set(a) & set(b))
    return newlist


if __name__ == "__main__":
    a = []
    b = []
    for i in range(0, 10):
        a.append(random.randint(1, 99))
    for i in range(0, 10):
        b.append(random.randint(1, 99))
    print(a)
    print(b)
    print(overlap(a, b))
    input()