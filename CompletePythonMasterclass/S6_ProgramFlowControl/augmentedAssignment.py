number = '9,112,556,572,198,773'
cleanedNumber = ''

for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumber += number[i]
        # this augmented assignment is actually more efficient in python

newNumber = int(cleanedNumber)
print('The number is {}'.format(newNumber))

x = 23
x += 1
print(x)

x -= 4
print(x)

x *= 5
print(x)

x /= 4
print(x)

x **= 2
print(x)

x %= 60
print(x)

greeting = 'Good '
greeting += 'morning '
print(greeting)

greeting *= 5
print(greeting)

# += -= *= .....
