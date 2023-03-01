#! python3
#
# Surface area of a cone
# Find the surface area of a cone given the height and the radius.
# You will need to ask the user to enter in both variables, and will 
# need to use the Pythagorean relationship to find the slant height. 
# (2 points)
#
# Inputs:
# height, radius
#
# Outputs:
# surface area
#
# Test output
# r = 3
# h = 5
# sa = 83.2297607912

import math
A = 0.0

print("This calculator will find the surface area of a cone given its height and radius\n")

def Calculate(H, R):
    global A
    A = math.pi * R * (R+((H**2)+(R**2))**0.5)

def SolveEq():
    h = float(input("\nEnter the height of the cone:\n"))
    if 0 >= h:
        print("Well now that's not a real measurement")
        SolveEq()
    r = float(input("Enter the radius of the base of the cone:\n"))
    if 0 >= r:
        print("Well now that's not a real measurement")
        SolveEq()
    Calculate(h, r)
    print("The surface area of this cone is: ", A)
    SolveEq()

SolveEq()