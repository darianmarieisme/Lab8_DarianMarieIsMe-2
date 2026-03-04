'''Lab 8 Option 2
Darian Marie Bruce
This program calculates the area of perimeter of circles
and rectangles
03/03/2026'''

menu: bool = True
invalid_menu_input: bool = True
invalid_input: str = "Invalid input. Please try again."

#color codes ansi escape sequences

orange: str = "\033[38;5;208m"
purple: str = "\033[38;5;129m"
reset: str = "\033[0m"

while menu:
    print("Geometry Calculator")
    print("-"*19)
    print(
    f"\n{orange}1.{reset} Calculate Circle Area",
    f"\n{orange}2.{reset} Calculate Circle Circumference",
    f"\n{orange}3.{reset} Calculate Rectangle Area",
    f"\n{orange}4.{reset} Calculate Rectangle Perimeter",
    f"\n{orange}5.{reset} Exit\n ")

    while invalid_menu_input:
            user_input: str = input(f"\nEnter your choice ({orange}1-5{reset}): ")
            
            if user_input.isdigit():
                  menu_option: int = int(user_input)

            if 1 <= menu_option <= 5:
                 invalid_menu_input = False

            else:
                 print(invalid_input)

    break