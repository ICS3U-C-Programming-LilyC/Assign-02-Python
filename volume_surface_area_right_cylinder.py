#!/usr/bin/env python3

# Created by: Lily Carroll
# Created on: Sept/25/2023
# This program calculates the volume and the surface area of a right cylinder with user 
# input.
# Importing the math module and my constants from my constants.py file. 
import math
import constants

def main():
  # Explaining my program to the user.
  print("This program will calculates the surface area and volume of a right cylinder.")
  
  # Telling user the 3 options they can choose from for their calculation.
  print("The units of calculation that you may choose from are:") 
  print("1 - centimeters")
  print("2 - millimeters")
  print("3 - meters")

  # Getting the userinput for the units.
  unit_choice = input(
    "Please enter the number representing the unit of measurement that you would like to use: ")
  
  # Using if then, elif and else to allow user to choose from the unit options.
  # If the units chosen are cm, then do the calculations using centimeters.
  if unit_choice == "1":
    unit = constants.UNIT_CENTIMETERS

  # Else if the units chosen are mm, then do the calculations using millimeters.
  elif unit_choice == "2":
    unit = constants.UNIT_MILLIMETERS

  # Else if the units chosen are m, then do the calculations using meters. 
  elif unit_choice == "3":
    unit = constants.UNIT_METERS

  # Else display the error message that the units chosen are not valid.
  else:
    print("Invalid units. Please select one from the options above.")
    exit()

    # Declaring variables.
  radius = float(input("Enter a radius of a right cylinder: "))
  height = float(input("Enter a height of a right cylinder: "))

# Calculating the volume and surface area.
  volume = math.pi * radius ** 2 * height
  surface_area = 2 * math.pi * radius * height + 2 * math.pi * radius ** 2

# Error checking for a input of 0, using an if statement.
  if radius == 0 or height == 0:
    print("Please enter a valid number")

# Error checking for a negative number input using an elif statement.
  elif radius < 0 or height < 0:
    print("Please enter a valid number")
    
# Printing the volume and surface area of the cylinder.
  else:
    print("The volume of the right cylinder is = {:.2f} {}^3". format (volume, unit))
    print("The surface area of the right cylinder is = {:.2f} {}^2". format(surface_area, unit))


if __name__ == "__main__":
  main()
