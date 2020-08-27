
""" Question 1"""
NAME_OUT_FILE = "name.txt"

name_file = open(NAME_OUT_FILE, 'w')
user_name = input('Enter your name here --> ')
print(user_name, file=name_file)
name_file.close()

"""Question 2"""
name_file = open(NAME_OUT_FILE, 'r')
name = name_file.read().strip()
name_file.close()
print('Your name is', name)


"""Question 3"""

numbers_file = open('numbers.txt', 'r')
number1 = int(numbers_file.readline())
number2 = int(numbers_file.readline())
numbers_file.close()

print(number1 + number2)

"""Question 4"""

numbers_file = open('numbers.txt', 'r')
total_number = 0
for line in numbers_file:
    number = int(line)
    total_number += number
numbers_file.close()

print(total_number)