
MENU = " 1) Add\n 2) Subtract\n 3) Multiply\n 4) Divide"

def main():
    print("Welcome to Clean Calculator!")
    loop_controller = 0
    while loop_controller == 0:
        print(MENU)

        menu_input = int(input(">>>"))

        if menu_input == 1:
            print("adding")
            loop_controller = 1
        elif menu_input == 2:
            print("subtracting")
            loop_controller = 1
        elif menu_input == 3:
            print("multipling")
            loop_controller = 1
        elif menu_input == 4:
            print("dividing")
            loop_controller = 1
        else:
            print("invalid entry")

main()