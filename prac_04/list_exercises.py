
"""list expercises"""


def main_01():

    print_numbers(fetch_numbers())


def fetch_numbers():
    numbers = []
    for a in range(0,5):
        numbers.append(int((input("Number: "))))
    return numbers

def print_numbers(numbers):
    print("The first number is {}".format(numbers[0]))
    print("The last number is {}".format(numbers[-1]))
    print("The smallest number is {}".format(min(numbers)))
    print("The largest number is {}".format(max(numbers)))
    print("The average of the numbers is ", sum(numbers) / len(numbers))

def main_02():

    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
    name = input("Username: ")
    if name in usernames:
        print("Access granted")
    else:
        print("Access denied")


main_02()