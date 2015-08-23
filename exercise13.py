# Fibonacci sequence. Asks user for how many numbers. 

def fib(num):
    fibnum = []
    a, b = 0, 1
    count = 0
    while count < num:
        fibnum.append(b)
        a, b = b, a + b
        count += 1
    return fibnum


if __name__ == "__main__":
    print("Generate how many numbers? Input must be integer. ")
    num = int(input())
    print(fib(num))
    