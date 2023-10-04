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
    y1, y2 = input("Enter two values: ").split()
    x1, x2 = input("Enter two values: ").split()

    m = y2-y1/x2-x1
    a = math.sqrt(((x2-x1)**2)+((y2-y1**2)))
    print(a)
six()
    


#CREDIT:SkeletalDemise told me to learn functions, it made it so much easier, now I don't have to go through the whole script every time :P

