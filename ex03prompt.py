# Prompt the user for a number and find which are smaller than it.
# In a list.

original = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newlist = []
print("Original list", original)
num = int(input('Find numbers smaller than: '))
for number in original:
    if number < num:
        newlist.append(number)
print(newlist)
input()
