'''Lab 8 Option 2
Darian Marie Bruce
This program calculates the area of perimeter of circles
and rectangles
03/03/2026'''

#importing functions with alias naming to prevent conflicts
#because area is used in both circle and rectangle

import circle as c

import rectangle as r

#frequently used strings, while loop set to true

menu: bool = True
invalid_input: str = "Invalid input. Please try again."
radius_input: str = "Enter the radius of the circle: "
height_input: str = "Enter the height of the rectangle: "
width_input: str = "Enter the width of the rectangle: "
area_string: str = "The area is: "

#color codes ansi escape sequences

orange: str = "\033[38;5;208m"
purple: str = "\033[38;5;129m"
reset: str = "\033[0m"

press_enter: str = f"Press Enter to {purple}continue{reset}..."

#function to check for valid input

def check_input(prompt: str):
    while True:
        user_input = input(prompt)

        if user_input.isdigit():
            number = int(user_input)
            if number > 0:
                return int(user_input)
            else:
                print(invalid_input)
                continue
        else:
            print(invalid_input)
            continue


#main program

while menu:
    print("Geometry Calculator")
    print("-"*19)
    print(
    f"\n{orange}1.{reset} Calculate Circle Area",
    f"\n{orange}2.{reset} Calculate Circle Circumference",
    f"\n{orange}3.{reset} Calculate Rectangle Area",
    f"\n{orange}4.{reset} Calculate Rectangle Perimeter",
    f"\n{orange}5.{reset} Exit\n ")

    invalid_menu_input: bool = True

    while invalid_menu_input:
            menu_option = check_input(f"\nEnter your choice ({orange}1-5{reset}): ")
            #check menu options are in range
            if 1 <= menu_option <= 5:
                invalid_menu_input = False 
            else:
                print(invalid_input)
                continue

    if menu_option == 1:
        print(" ")
        radius = check_input(radius_input)
        circle_area = c.area(radius)
        print(area_string,circle_area)
    elif menu_option == 2:
        print(" ")
        radius = check_input(radius_input)
        circle_circumference = c.circumference(radius)
        print(f"The circumference is: {circle_circumference}")
    elif menu_option == 3:
        print(" ")
        width = check_input(width_input)
        height = check_input(height_input)
    elif menu_option == 4:
        print(" ")
        width = check_input(width_input)
        height = check_input(height_input)
    else:
        menu: bool = False

#press enter to continue after menu logic runs

    if menu_option in range(1,5):
        print(" ")
        input(press_enter)
        print(" ")
        menu_option = None
        continue