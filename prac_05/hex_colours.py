
"""look up hex colours"""

"""constant dictionary"""

HEX_COLOURS = {"aliceblue": "#f0f8ff", "antiquewhite": "#faebd7",
                "antiquewhite1": "#ffefdb", "antiquewhite2": "#eedfcc",
                "antiquewhite3": "#cdc0b0", "antiquewhite4": "#8b8378",
                "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6",
                "aquamarine4": "#458b74", "azure1": "#f0ffff",
                "azure2": "#e0eeee", "azure3": "#c1cdcd", "azure4": "#838b8b",
                "beige": "#f5f5dc", "bisque1": "#ffe4c4"}

"""Main"""

def main():
    colour = input("Enter short colour: ").lower()   #<--- use .upper() to change to all entries to capital
    while colour != "":
        if colour in HEX_COLOURS:
            print(colour, "is", HEX_COLOURS[colour])
        else:
            print("Invalid colour")
        colour = input("Enter short colour: ").lower()


main()