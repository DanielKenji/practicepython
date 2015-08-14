# Checks if a number is prime. 

def prime(num):
    div = 1
    while div != (num // 2) + 1:
        div += 1
        if num % div == 0:
            return False
    return True

if __name__ == "__main__":
    num = int(input("Enter a number: "))
    print(prime(num))
    input()