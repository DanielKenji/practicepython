# Remove duplicates in a list. Using loops and using sets.

def remdup1(L):
    newlist = []
    for element in L:
        if element not in newlist:
            newlist.append(element)
    return newlist
    
def remdup2(L):
    newlist = list(set(L))
    return newlist
