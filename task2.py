#! python3
# Find the volume of a sphere.
# You will ask the user to enter the radius of the sphere.
# Calculate the Volume and then display the result to the user.
# You will need to import the math module in order to use math.pi

# Inputs:
# radius
#
# Outputs
# volume
#
# test output radius of 3 should give volume of 113.09733552923254

import math
Radius = 0.0
Volume = 0.0

print("\nThis program will calculate the volume of a sphere given its radius")

def Request():
    global Radius
    Radius = float(input("What is the radius of your sphere?\n"))

def Calculate(r):
    global Volume
    Volume = ((r)**3)*(math.pi)*(4 / 3)

def Sphere():
    print("\n")
    Request()
    Calculate(Radius)
    print("The Volume of your sphere is: ", Volume)
    Sphere()

Sphere()