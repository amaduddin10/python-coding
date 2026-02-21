a = int(input('enter you first number'))
b = int(input('enter you second number'))
c = int(input('enter you third number'))

if a > b and a > c:
    print('the greatest number is:' , a)

elif b > a and b > c:
    print('the greatest number is:' , b)

else:
    print('the greatest number is:' , c)