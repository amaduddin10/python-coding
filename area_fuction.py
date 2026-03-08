def  triangleAREA(base,height):
    area = (base*height)/2
    return area

def squarearea(side):
    area = side ** 2 
    return area

def rectanglearea(lenght,width):
    area = lenght * width
    return area

def circlearea(radius):
    area = 3.14159 * radius * 2
    return area

print('Area calculator')
print('chose a shape')
print('1.rectangle area')
print('2.triangle area')
print('3.squre area')
print('4.cicle area')

choise = input('enter your choise from (1/2/3/4)')

if choise == '1':
    l = float(input('enter the lenght of rectangle'))
    w = float(input('enter the width of rectangle'))
    print('the area of rectangle is:' , rectanglearea(w,l))

elif choise == '2':
    b = float(input('enter the base of triangle'))
    h = float(input('enter the height of triangle'))
    print('the area of triangle is:' , triangleAREA(b,h))

elif choise == '3':
    s = float(input('enter the side of square'))
    print('the area of squre is:' , squarearea(s))

elif choise == '3':
    r = float(input('enter the radius of circle'))
    print('the area of circle is:' , circlearea(r))

else:
    print('invalid input!')