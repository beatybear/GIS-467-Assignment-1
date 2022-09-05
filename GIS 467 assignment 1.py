# -*- coding: utf-8 -*-
"""
CS 467/667 Assignment 1

1. Write code that stores a first name in one variable and a last name in a second and prints a statement:
    My name is Tara Dactyl
2. Building on #1, use a variable to store a zip code (or other numeric value) and print a message like the following:
    My name is Tara Dactyl, I live in 92373!
3. Write one expression for each of the following arithmetic operators (6 lines): 
    + , - , * , /, **, %
4. Using variables for the radius and pi, write a few lines of code that will calculate the area of a circle. 
5. Write Python code that convert a distance in feet to meters
    1) Create a variable for a distance in feet
    2) Calculate the distance in meters and store the result as a new variable
    3) Print the value of the distance in meters variable

"""

class assignmentOne:
    # 1. write a code that stores a first name in one variable and a last name in a second and prints a statement
    print("1.")
    firstN = "Grace"
    lastN = "Beaty"
    print("My name is " + firstN + " " + lastN + ".\n")
    
    # 2. building on #1, use a variable to store a zip code (or other numeric value) and print a message like the following:
    print('2.')
    zipCode = 91784
    print("My name is " + firstN + " " + lastN + ", I live in " + str(zipCode) + "!\n")
    
    # 3. write one expression for each of the following arithmetic operators: +, -, *, /, **, %
    print('3.')
    print("Each expression should be equal to 4")
    print('1 + 3 = ' + str(1 + 3))
    print('9 - 5 = ' + str(9 - 5))
    print('4 * 1 = ' + str(4 * 1))
    print('24 / 6 = ' + str(24 / 6))
    print('2 ** 2 = ' + str(2 ** 2))
    print('24 % 5 = ' + str(24 % 5) + "\n")
    
    # 4. using variables for the radius and pi, write a few lines of code that will calculate the area of a circle
    print('4.')
    radius = 4
    pi = 3.14159
    area = pi * (radius**2)
    print("The area of a circle with radius, " + str(radius) + ", is " + str(area) + ".\n")
    
    # 5. write a python code that converts a distance in feet to meters
    print('5.')
    distanceFt = 6
    distanceM = distanceFt/3.28 #3.28 feet in a meter
    print(str(distanceFt) + " feet is " + str(distanceM) + " meters.\n")
    