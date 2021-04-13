numbers = []
n = 1
while n <= 5:
    number = float(input("Number: "))
    numbers.append(number)
    n += 1
max_number = max(numbers)
min_number = min(numbers)
first_number = numbers[0]
last_number = numbers[4]
ave_number = sum(numbers) / 5
print("The first number is {:.2f}".format(first_number))
print("The last number is {:.2f}".format(last_number))
print("The largest number is {:.2f}".format(max_number))
print("The smallest number is {:.2f}".format(min_number))
print("The average number is {:.2f}".format(ave_number))
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = str(input("Enter your name: "))
if username in usernames:
    print("Access granted")
else:
    print("Access denied")
