weitgh = float(input('enter your kg:'))
heitgh = float(input('enter your meter:'))

bmi = weitgh / heitgh **2 

print('your bmi is:' , bmi)

if bmi < 18.5:
    print('you are underweitgh. you need to get some weitgh')

elif 18.5 <= bmi <= 24.9:
    print('you are normal in weitgh. keep it up!')

elif 25 <= bmi <= 29.9:
    print('you are overweitgh. you need to lose some weitgh')

elif 30 <= bmi <= 34.9:
    print('you are obse. lossing weitgh is emergency')

else:
    print('you are extremly obese. pls visit the doctor as sonn as posible')