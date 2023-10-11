#!/usr/bin/env python3

# Created by: Lily Carroll
# Created on: Sept/25/2023
# This program calculates the volume and the surface area of a right cylinder with user 
# input.
import math

def main():
  # Explaining my program to the user.
  print("This program will calculates the surface area and volume of a right cylinder.")

# Getting the radius and height of the cylinder from user.
  print("This program calculates the volume and")
  print("surface area of a right cylinder.")

  # Declaring variables.
  radius = float(input("Enter a radius of a right cylinder: "))
  height = float(input("Enter a height of a right cylinder: "))

# Calculating the volume and surface area.
  volume = math.pi * radius ** 2 * height
  surface_area = 2 * math.pi * radius * height + 2 * math.pi * radius ** 2

# Error checking for a input of 0, using an if statement.
  if radius == 0 or height == 0:
    print("Please enter a valid number")

  else:
    print("")
    print("The volume of the right cylinder is = {:.2f}". format (volume))
    print("The surface area of the right cylinder is = {:.2f}". format(surface_area))


if __name__ == "__main__":
  main()
