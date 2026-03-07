def calculator(choice,a,b):
    if choice == 1:
        return a + b 
    elif choice == 2: 
        return a - b
    elif choice == 3:
        if b == 0:
            return 'Error! Division by zero is not allowed'
        return a/b
    else:
        return 'invalid choice'
    
print('---------Calculator----------')
print('1. addtion')
print('2. subtraction')
print('3. multyplication')
print('4. division')
print('-----------------------------')

choice=int(input('enter choice (1/2/3/4)'))

a=float(input('enter your first number'))
b=float(input('enter your second number'))

result = calculator(choice, a, b)
print('-----------------------------')
print('result', result)
print('-----------------------------')