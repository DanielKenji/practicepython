# Divisors with list comprehension.

def divisors(num):
    divs = num//2 + 1
    divlist = [i for i in range(1, divs) if num%i == 0]
    return divlist

if __name__ == "__main__":
    num = int(input())
    print(divisors(num))
    input()