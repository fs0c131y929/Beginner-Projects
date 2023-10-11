#Hello, this program will calculate the properties of a triangle given by inputs of the user.
#Below, this first section will collect input.

import math

side_a = float(input('Please enter the length of side A of the triangle in meters: '))
side_b = float(input('Please enter the length of side B of the triangle in meters: '))
side_c = float(input('Please enter the length of side C of the triangle in meters: '))

#This section calculates the perimeter and area of the trinangle.

triangle_perimeter = side_a + side_b + side_c 
print('The perimeter of the triangle is:', triangle_perimeter,'m')

semi_perimeter = (side_a + side_b + side_c) / 2    

area = math.sqrt(semi_perimeter * (semi_perimeter - side_a) * (semi_perimeter - side_b) * (semi_perimeter - side_c))
print('The area of the triangle is:', area,'m^2')

#This section determines the type of triangle. (obtuse, acute, right)

if side_c >= side_a + side_b:
    print('It is an obtuse triangle.')

elif side_c == side_a + side_b:
    print('It is a right triangle.')

elif side_c <= side_a + side_b:
    print('This is an acute triangle.')    



