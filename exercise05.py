# Takes two lists and return another with the elements that are
# common between them.

def overlap(a, b):
    newlist = []
    for x in a:
        for y in b:
            if x == y and x not in newlist:
                newlist.append(x)
    return newlist