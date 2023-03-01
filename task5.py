#! python3
#
# Find the radius of a sphere if you are given the volume.
# Think about how you would need to solve this equation if you were doing it on paper
#
# Inputs:
# Volume (float)
#
# Outputs:
# radius (float)
#
# Test output Volume of 20.22 should give radius of:1.69002229118
# Note: You will need to do some strange things with your cube root.
# Remember that a cube root is the same as an exponent of 1/3, but
# here you will need to do a power of 1.0/3 or something strange happens.

import math
V = 0.0
r = 0.0

print("\nThis calculator will find the radius of a perfect sphere given its volume\n")

def Calculate(x):
    global r
    r = ((x * 0.75) / math.pi)**(1.0/3.0)

def SolveEq():
    global V
    V = float(input("\nEnter the volume of the sphere:\n"))
    if 0 >= V:
        print("Well now that's not a real measurement")
        SolveEq()
    Calculate(V)
    print("The radius of this sphere is: ", r)
    SolveEq()

SolveEq()