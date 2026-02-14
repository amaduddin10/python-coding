last = float(input('enter your last mounth reading'))
current = float(input('enter current mounth reading '))

unit = current - last

bill = 0 

if unit > 400:
    bill = bill + (unit + 400) * 15
    unit = 400

if unit > 200:
    bill = bill + (unit + 200) * 10
    unit = 200

if unit > 100:
    bill = bill + (unit + 100) * 7
    unit = 100

bill = bill + unit * 5

print('total unit Cunsumed:' , unit)

print('Total bill:' , bill)