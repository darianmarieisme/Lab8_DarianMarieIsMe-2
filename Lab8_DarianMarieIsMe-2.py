'''Lab 8 Option 2
Darian Marie Bruce
This program calculates the area of perimeter of circles
and rectangles
03/03/2026'''

menu: bool = True

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
    f"\n{orange}5.{reset} Exit\n \n ")

    menu_option: int = int(input(f"\nEnter your choice ({orange}1-5{reset}): "))

    break