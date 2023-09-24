import os
import time
import math

# Day 2: 30 Days of python programming
first_name = 'Jason'
last_name = 'Sawyer'
full_name = 'Jason Sawyer'
country = 'Australia'
city = 'Sydney'
age = '21'
year = '2023'
is_married = False # i wish lol
is_true = True
is_light_on = True
q1, q2, q3 = 'a', 'b', 'c'

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))
print(type(q1))
print(type(q2))
print(type(q3))
time.sleep(2)
os.system('clear')
print(len(first_name))
print(len(last_name))

num_one = 5
num_two = 4
x = num_one + num_two
y = num_two - num_one
z = num_two * num_one
a = num_one / num_two
remainder = num_two % num_one
exp = num_one**num_two
floor_division = num_one // num_two

radius_of_circle = 30
area_of_circle = math.pi * radius_of_circle**2
circum_of_circle = 2 * math.pi * radius_of_circle

os.system("clear")
print("Area of circle calculator")
radius_of_circle = input("Input radius: ")
area_of_circle = math.pi * float(radius_of_circle)**2
print(f"The area of the circle is: {(area_of_circle)}")
time.sleep(2)
os.system("clear")

del first_name, last_name, full_name, country, city, age

first_name = input("What is your first name: ")
last_name = input("What is your last name: ") 
full_name = input("What is your full name: ")
country = input("What country are you from: ")
age = input("What is your age: ")
