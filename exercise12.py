# Return the first and last elements in a list

def listends(a):
    newlist = []
    newlist.append(a[0])
    if len(a) > 1:
        newlist.append(a[-1])
    return newlist

