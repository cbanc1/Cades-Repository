#----------------------# Cade Bancroft, Exercise 1 #-------------------------------#
import math
#--------------------------------# Done #------------------------------------------#
def absolute(x):
    """
    Determine the absolute value of a number
    """
    if x > 0:
        return x
    elif x < 0:
        return -x
    else:
        return 0

#----------------------------------------------------------------------------------#
def quotient(x, y):
    """
    Determine the quotient of the fraction: x/y
    """
    
#--------------------------------# Done #------------------------------------------#
def distance(x1, y1, x2, y2):
    """
    Determine the distance between 2 points on a graph
    """
    deltaX = 0
    deltaY = 0
    if x1 > x2: #Determining Delta X
        deltaX = (x1 - x2)
    elif x1 < x2:
        deltaX = (x2 - x1)
    else:
        deltaX = x1
        
    if y1 > y2: #Determining Delta Y
        deltaY = (y1 - y2)
    elif y1 < y2:
        deltaY = (y2 - y1)
    else:
        deltaY = x1

    d = (deltaX**2) + (deltaY**2)
    return math.sqrt(d)

#--------------------------------# Done #------------------------------------------#
def cosine(a, b, C):
    """
    Determine "c" using the cosine law
    """
    C = math.radians(C)
    c = math.sqrt((a**2) + (b**2) - (2*a*b)*(math.cos(C)))
    return c

#--------------------------------# Done #------------------------------------------#
def quadratic(a, b, c):
    """
    Determine the 2 "x" values using the quadratic formula
    """
    if math.sqrt((b**2) - (4*a*c)) < 0:
        print("No Solutions")
    else:
        x1 = (-b + math.sqrt((b**2) - (4*a*c)))/(2*a)
        x2 = (-b - math.sqrt((b**2) - (4*a*c)))/(2*a)
        print(x1)
        print(x2)
