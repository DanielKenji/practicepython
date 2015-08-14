# Return elements in a list that are less than 5


def lessfive(a):
    newlist = []
    for element in a:
        if type(element) == int or type(element) == float and element < 5:
            newlist.append(element)
    return newlist

# In one line of Python:
# newlist = [i for i in a if i < 5]
# Of course, strings in the list will return an error
