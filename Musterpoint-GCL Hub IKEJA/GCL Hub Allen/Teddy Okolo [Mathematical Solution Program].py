#Okolo Teddy
#okolotedd@gmail.com
#GCL Hub, Ikeja Centre
#MATHapp

import math
print('Welcome to MATHapp!')
print('Welcome to the Mathematical Solution Program')

print('Select the mathematical problem of your choice and input the required parameters')

math_problem = input("Select a mathematical problem of your choice: \n(a) Quadratic \n(b) Sphere surface area \n(c) Arc Length \n(d) Area of an Octagon \n(e) Directrix of a parabola \n(f) Focus of a parabola \n(g) Pearson Correlation \n ")

if (math_problem) == 'a':
    a = float(int(input('Enter coefficient of a: ')))
    b = float(int(input('Enter coefficient of b: ')))
    c = float(int(input('Enter coefficient of c: ')))
    r1 = 'root1'
    r1 = (-b) + (math.sqrt(abs(float(b ** 2) - (4 * a * c))))
    r1 = round(r1, 2)
    r2 = 'root2'
    r2 = (-b) - (math.sqrt(abs(float(b ** 2) - (4 * a * c))))
    r2 = round(r2, 2)
    print('The first root is:', r1)
    print('The second root is:', r2)
    
elif (math_problem) == 'b':
    r = float(int(input('Enter value for radius of the sphere: ')))
    x = 'surface area'
    x = 4 * (math.pi * (r ** 2))
    x = round(x, 2)
    print('The surface area of the sphere is:', x)

elif (math_problem) == 'c':
    r = float(int(input('Enter value for radius of the circle: ')))
    t = float(int(input('Enter value for the arc angle: ')))
    x = 'arc length'
    x = 2 * ((math.pi) * r) * (t / 360)
    x = round(x, 2)
    print('The length of the arc is:', x)

elif (math_problem) == 'd':
    a = float(int(input('Enter value of side: ')))
    x = 'Octagon area'
    x = (2 * (a ** 2)) * (1 + (math.sqrt(2)))
    x = round(x, 2)
    print('The area of the octagon is:', x)

elif (math_problem) == 'e':
    a = float(int(input('Enter coefficient of a: ')))
    b = float(int(input('Enter coefficient of b: ')))
    c = float(int(input('Enter coefficient of c: ')))
    x = 'Directrix'
    x = c - (((b ** 2) + 1) * 4 * a)
    x = round(x, 2)
    print('The directrix of the parabola is:', x)

elif (math_problem) == 'f':
    a = float(int(input('Enter coefficient of a: ')))
    b = float(int(input('Enter coefficient of b: ')))
    c = float(int(input('Enter coefficient of c: ')))
    x1 = 'Point A'
    x2 = 'Point B'
    x1 = (-b) / (2 * a)
    x1 = round(x1, 2)
    x2 = ((4 * a * c) - (b ** 2) + 1) / (4 * a)
    x2 = round(x2, 2)
    print('The focal points of the parabola are:', x1 , x2)

elif (math_problem) == 'g':
    n = float(int(input('Enter the total number of values: ')))
    x = float(int(input('Enter the sum of x values of the set data: ')))
    y = float(int(input('Enter the sum of y values of the set data: ')))
    x2 = float(int(input('Enter the sum of the squared x values of the set data: ')))
    y2 = float(int(input('Enter the sum of the squared y values of the set data: ')))
    xy = float(int(input('Enter the sum of the xy product values of the data set: ')))
    r1 = 'numerator'
    r2 = 'denominator'
    r1 = (n * xy) - (x * y)
    r2 = math.sqrt(((n * x2) - (x ** 2)) * ((n * y2) - (y ** 2)))
    r = 'Pearson correlation coefficient'
    r = r1 / r2
    r = round(r, 3)
    print('The Pearson correlation coefficient is:', r)
    
    

    
    
    
