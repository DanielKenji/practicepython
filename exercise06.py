# Verifies if the string is a palindrome. Return True or False

def palindrome(string):
    newstring = ''
    newstring = string.lower()
    trans = str.maketrans("!',.?;:", "       ")
    newstring = newstring.translate(trans)
    newstring = newstring.replace(' ', '')
    if newstring == newstring[::-1]:
        return True
    else:
        return False

if __name__ == "__main__":
    print("Enter a string: ")
    string = input()
    print(palindrome(string))
    input()
