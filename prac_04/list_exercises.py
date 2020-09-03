
"""list expercises"""

def main():

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

main()