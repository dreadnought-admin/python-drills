
import sys

def check_py():
    a = int(input("Enter the length of side a: "))
    b = int(input("Enter the length of side b: "))
    c = int(input("Enter the length of side c: "))
    if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or c**2 + a**2 == b**2:
        print("The triangle is a Pythagorean Triple.")
        restart = input(("Press 'X' to quit or 'R' to try again:\n ")).capitalize()
        if restart == "X":
            sys.exit(-1)
        elif restart == "R":
            check_py()
    else:
        print("The triangle is not a Pythagorean Triple.")
        restart = input(("Press 'X' to quit or 'R' to try again:\n ")).capitalize()
        if restart == "X":
            sys.exit(-1)
        elif restart == "R":
            check_py()

check_py()