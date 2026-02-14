cause = input('do you have medical reason yes/no: ').lower()

if cause == 'yes':
    attendance=int(input('enter your attendance percentage'))

    if attendance >= 60:
        print('you are allowed to give exam.')
    else:
        print('you are not allwed to give exam.')

elif cause == 'no':
    attendance=int(input('enter your attendance percentage'))

    if attendance >= 75:
        print('you are allowed to give exam.')
    else:
        print('you are not allwed to give exam.')

else:
    print('invalid input')