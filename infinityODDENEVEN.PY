while True:
    n=input('enter a number or exit to quit:').lower()

    if n=='exit':
        print('exeting program')
        break

    else:
        n = int(n)
        if n % 2 == 0:
            print('is even')
        else:
            print('is odd')