"""When naming variables in python,we use  the (snake_case) naming convention.The underscore is used if te variable name is more than one word"""

# Write a python comment saying 'Day 2: 30 Days of python programming' 
        # 'Day 2: 30 days of python programming'
#  Declare a first name variable and assign a value to it
from itertools import product


first_Name="Conslate"
print(first_Name)
# Declare a last name variable and assign a value to it
last_Name="koyo"
print(last_Name)
# Declare a full name variable and assign a value to it
full_Name="conslate koyo"
print(full_Name)
# Declare a country variable and assign a value to it
country="Kenya"
print(country)
# Declare a city variable and assign a value to it
city="Nairobi"
print(city)
# Declare an age variable and assign a value to it
age= 35
print(age)
# Declare a year variable and assign a value to it
year=2022
print(year)
# Declare a variable is_married and assign a value to it
is_married=True
print(is_married)
# Declare a variable is_true and assign a value to it
is_true="probably"
print(is_true)
# Declare a variable is_light_on and assign a value to it
is_light=50
# Declare multiple variable on one line
print(first_Name,last_Name,age,country,city)
# Check the data type of all your variables using type() built-in function
print(type(first_Name))
print(type(last_Name))
print(type(full_Name))
print(type(country))
print(type(city))
print(type(age))
print(type(is_true))
print(type(is_light))
# Using the len() built-in function, find the length of your first name
print(len(first_Name))
# Compare the length of your first name and your last name
print(len(first_Name)!=len(last_Name))
# Declare 5 as num_one and 4 as num_two
num_one=5
print(num_one)
num_two=4
print(num_two)
# Add num_one and num_two and assign the value to a variable total
total=num_one+num_two
print(total)
# Subtract num_two from num_one and assign the value to a variable diff
diff=num_one-num_two
print(diff)
# Multiply num_two and num_one and assign the value to a variable product
product=num_two*num_one
print(product)
# Divide num_one by num_two and assign the value to a variable division
division=num_two/num_one
print(division)
# Use modulus division to find num_two divided by num_one and assign the value to a variable remainder
remainder=num_two%num_one
print(remainder)
# Calculate num_one to the power of num_two and assign the value to a variable exp
exp=num_one**num_two
print(exp)
# Find floor division of num_one by num_two and assign the value to a variable floor_division
floor_division=num_one//num_two
# The radius of a circle is 30 meters.
# Calculate the area of a circle and assign the value to a variable name of area_of_circle
radius=30
area_of_a_circle=3.142*(radius**2)
print(area_of_a_circle)
# Calculate the circumference of a circle and assign the value to a variable name of circum_of_circle
circum_of_circle=3.142*(2*radius)
print(circum_of_circle)
# Take radius as user input and calculate the area
from math import pi
radi=int(input("radius_Of_A_Circle: "))
area=pi*(radi**2)
print(area)

# Use the built-in input function to get first name, last name, country and age from a user and store the value to their corresponding variable names
a=str(input("first_name: "))
print(a)
b=str(input("last_name: "))
print(b)
c=str(input("country: "))
print(c)
d=int(input("age: "))
print(d)


# Run help('keywords') in Python shell or in your file to check for the Python reserved words or keywords

