# Number odd or even. Also if it's a multiple of 4.

num = int(input('Enter a number: '))
if num % 2 == 0:
    print(num, 'is even.')
    if num % 4 == 0:
        print(num, 'is a multiple of 4.')
else:
    print(num, 'is odd.')
input()
