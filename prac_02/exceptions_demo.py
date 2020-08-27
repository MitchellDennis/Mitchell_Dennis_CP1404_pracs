

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    if denominator == 0:
        print('denominator must be non zero')
    else:
        fraction = numerator / denominator
        print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")

print("Finished.")



""" Answers to Questions:
1) When a the numerator and/or denominator is not an intiger
2) When a 0 is entered in the denominator
3) By putting an if statement to catch a non zero entry????"""