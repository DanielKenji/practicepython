# Reverse word order of a string

def rev(a):
    temp = a.split()
    temp.reverse()
    new = " ".join(temp)
    return new
    
if __name__ == "__main__":
    a = input("Enter a phrase: ")
    print(rev(a))
    input()