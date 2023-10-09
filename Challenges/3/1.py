import math

age = 21
height = 170.0
compl = 4j

#
def one():
    b = float(input("Enter base: "))
    h = float(input("Enter height: "))
    var = int(b*h*0.5)
    print(f'The area of the triangle is', {var})

#
def two():
    a = float(input("Enter side a: "))
    b = float(input("Enter side b: "))
    c = float(input("Enter side c: "))
    perimeter = int(a + b + c)
    print(f'The perimeter of the triangle is', {perimeter})

#
def three():
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    area = int(length*width)
    perimeter = int(2*(length+width))
    print(f"The area is {area} and the perimeter is {perimeter}")

def four():   # this is question 7
    r = float(input("Enter the radius:"))
    pi = 3.14 # i would have imported math but it is stated in the github to make pi 3.14 https://github.com/Asabeneh/30-Days-Of-Python/blob/master/03_Day_Operators/03_operators.md#-exercises---day-3:~:text=pi%20x%20r)-,where%20pi%20%3D%203.14.,-Calculate%20the%20slope
    area = int(pi*r**2) # i used int as that is the precedent
    print(f'The area of the circle is', area)
#
def five():
    m = int(input("Enter in the value for m: "))
    b = int(input("Enter in the value for b: "))
    
    y = int(b)
    x = int((-b)/m)
    
    print(f'The slope is {m}\nThe x-intercept is {x}\nThe y-intercept is {y}')


def six():
    x1, y1 = input("Enter two values: ").split()
    x2, y2 = input("Enter two values: ").split()

    y1, y2, x1, x2 = float(y1), float(y2), float(x1), float(x2)  
    m = (y2-y1)/(x2-x1)
    a = math.sqrt((x2- x1) ** 2 + (y2 - y1) ** 2)
    print(f'The Euclidean distance between {x1},{y1} and {x2}, {y2} is {a}\nThe slope is {m}' )

def seven():
    slope1 = 2
    slope2 = 2

    print("Are slope1 and slope2 equal?")
    if slope1 == slope2:
        print("Slope1 and Slope2 are equal")
    else:
        print("Slope1 and Slope2 aren't equal")

def eight():
    for x in range(-100, 101):
        y = x**2 + 6*x + 9
        if y == 0:
            print(f'x = {x} if y = 0')
   
def nine():
    x = len("python")
    y = len("dragon")
    
    if x == y:
        print("python and dragon have the same amount of characters")
    else:
        print("python and dragon do not have same amount of characters")

def ten():
    sent = "I hope this course is not full of jargon."
    x = "jargon"
    if x in sent:
        print(f'{x} is in {sent}')
    else:
        print(f'{x} is not in {sent}')
def eleven():
    x = "on"
    y = "python"
    z = "dragon"
    if x not in y and z:
        print(f'There is no {x} in {y} and {z}')
    else:
        print(f'There is {x} in {y} and {z}')   
   

def twelve():
    x = str(float(len("python")))
    print(x)
    print(type(x))

def thirteen():
    Num = float(input("Enter number: "))
    Num1 = float(Num % 2)
    if Num1 == 0.0:
        print(f'{int(Num)} is even.')
    elif Num%1 == 0.0:
        print(f'{(int(Num))} is odd.')
    else:
        print(f'{((Num))} is odd.')

def fourteen():
    x = int(7//3)
    if x == int(2.7):
        print(f'{x} equals the int(2.7)')
    else:
        print(f'{x} does not equal int(2.7)')

def fifteen():
    a = type('10')
    b = type(10)

    if a == b:
        print("The type of '10' is equal to type of 10")
    else:
        print("The type of '10' is not equal to type of 10")

def sixteen():
    a = int(9.8)
    b = (10)

    if a == b:
        print(f'The int of 9.8 is equal to 10')
    else:
        print(f'The int of 9.8 is not equal to 10')

def seventeen():
    x = float(input("Enter hours: "))
    y = float(input("Enter rate per hour: "))
    z = x*y
    if z%1 == 0.0:
        z = int(z)
    else:
        z = float(z)
    print(f'Your weekly earning is {z}')

def eighteen():
    z = int(input("Enter number of years you have lived: "))
    s = 60*60*24*365*z
    print(f'You have lived for {s} seconds.')

def nineteen():
    for i in range(1, 6):
        print(i,i**0,i,i**2,i**3)
   
#CREDIT:SkeletalDemise told me to learn functions, it made it so much easier, now I don't have to go through the whole script every time :P
