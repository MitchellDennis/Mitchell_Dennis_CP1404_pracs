"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import shutil
import os


def main():
    """Demo os module functions."""
    print("Starting directory is: {}".format(os.getcwd()))

    # Change to desired directory
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current directory
    print("Files in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Make a new directory
    # The next time you run this, it will crash if the directory exists
    # Done: Use exception handling to avoid the crash (just pass)
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    # Loop through each file in the (current) directory
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))

        # Done: Try these options one at a time
        # Option 1: rename file to new name - in place
        # os.rename(filename, new_name)

        # Option 2: move file to new place, with new name
        # shutil.move(filename, 'temp/' + new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    # new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    new_name = str("")
    for position, character in enumerate(filename):
        previous_character = filename[position-1]
        if position == 0:
            new_name += character.upper()
        elif previous_character.islower() and character.isupper():
            new_name = new_name + str(" ")
            new_name = new_name + str(character)
        else:
            new_name = new_name + str(character)

    new_name = new_name.title().replace(" ", "_").replace(".TXT", ".txt").replace(".Txt", ".txt")
    return new_name


def demo_walk():
    """Process all subdirectories using os.walk()."""
    os.chdir('Lyrics')
    for directory_name, subdirectories, filenames in os.walk('.'):
        # print("Directory:", directory_name)
        # print("\tcontains subdirectories:", subdirectories)
        # print("\tand files:", filenames)
        # print("(Current working directory is: {})".format(os.getcwd()))


        for filename in filenames:
            full_name = os.path.join(directory_name, filename)
            new_name = os.path.join(directory_name, get_fixed_filename(filename))
            print(full_name)
            print(new_name)
            print("------------------------------------")
            # os.rename(full_name, new_name)
        #Had to look at answers for this one as i had my loop in the wrong spot and couldent get it to work. But i had the logic of the renaming right.


# main()
demo_walk()