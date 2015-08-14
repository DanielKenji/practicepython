# Practice Pyhton 4. Lists divisors of a number.

def divisors(num):
    divlist = [1]
    div = 1
    while div < (num//2 + 1):
        div += 1
        if num % div == 0:
            divlist.append(div)
    return divlist

if __name__ == "__main__":
    num = int(input())
    print("Divisors list: ")
    print(divisors(num))
    input()