"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
#print(CODE_TO_NAME)


"""loop to ask for state code and print state"""
# state_code = input("Enter short state: ").upper()   #<--- use .upper() to change to all entries to capital
#
# while state_code != "":
#     if state_code in CODE_TO_NAME:
#         print(state_code, "is", CODE_TO_NAME[state_code])
#     else:
#         print("Invalid short state")
#     state_code = input("Enter short state: ").upper()


"""Loop to neatly print names"""

for i in CODE_TO_NAME.keys():
    print("{} is {}".format(i, CODE_TO_NAME[i]))

