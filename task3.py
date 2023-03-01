#! python3

# Solve a two step algebra equation.
# Two steps equations are in the format ax + b = c
# You will ask the user to enter in all 3 variables: a, b and c
# You will need to display the solution for the equation

# inputs
# a, b, c
#
# outputs
# solution for x
#
# test case: 5, 1, 11 should give x = 2

import math
x = 0.0

print("This calculator will solve for x in equations of the form ax+b=c\n")

def Calculate(A, B, C):
    global x
    x = (C - B)/A

def SolveEq():
    a = float(input("\nEnter the value of a:\n"))
    b = float(input("Enter the value of b:\n"))
    c = float(input("Enter the value of c:\n"))
    Calculate(a, b, c)
    print("The value of x is: ", x)
    SolveEq()

SolveEq()