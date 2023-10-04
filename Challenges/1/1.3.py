import math
q1, q2 = input("Enter two values: ").split()  
print(f"{q1}, {q2}")
q = {q1 , q2}

p1, p2 = input("Enter two values: ").split() 
print(f"{p1}, {p2}")
p = {p1 , p2}


qp1 = int(q1) - int(p1) 
qp2 = int(q2) - int(p2)

qp3a = qp1**2
qp3b = qp2**2

result = math.sqrt((qp3a**2 + qp3b**2))
print(f"The Euclidean distance between the two points is: {result}")



