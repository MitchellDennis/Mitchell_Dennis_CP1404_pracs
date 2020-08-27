
"""Password checker"""
"""First version"""

MIN_LENGTH = 4

def main1():

    password = input("Enter your password of atleast {} characters: \n\r >>>".format(MIN_LENGTH))
    while len(password) < MIN_LENGTH:
        password = input("Enter your password of atleast {} characters: \n\r >>>".format(MIN_LENGTH))
    print('*' * len(password))
#main1()

def main():
    password = in_password_ref(MIN_LENGTH)
    print_asteriks(password)

def in_password_ref(min_len):
    password = input("Enter your password of atleast {} characters: \n\r >>>".format(min_len))
    while len(password) < MIN_LENGTH:
        password = input("Enter your password of atleast {} characters: \n\r >>>".format(min_len))
    return password

def print_asteriks(password):
    print('*' * len(password))


main()