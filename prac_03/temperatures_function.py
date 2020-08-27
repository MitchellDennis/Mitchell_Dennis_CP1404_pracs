

"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit = c_to_f(float(input("Celsius: ")))
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            celsius = f_to_c(float(input("Fahrenheit: ")))
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def c_to_f(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return(fahrenheit)

def f_to_c(fahrenheit):
    celsius = 5 / 9 * (fahrenheit - 32)
    return(celsius)

main()