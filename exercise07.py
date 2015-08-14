# Take a list and return only even elements in another list

def evenlist(a):
    numbers = [i for i in a if type(i) == int or type(i) == float]
    newlist = [i for i in numbers if i%2 == 0]
    return newlist
