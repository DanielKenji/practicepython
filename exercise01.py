# exercise 1 Practice Python. Modified to tell how many years till 100


name = input('Enter your name: ')
age = int(input('Enter your age: '))
if age == 100:
    print("Congratulations,", name, "you are 100 years old!")
else:
    time = 100 - age
    print("You will turn 100 years old in", time, "years")
input()