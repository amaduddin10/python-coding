buy = int(input('enter your buying price:'))
sell = int(input('enter your seling price:'))

if sell > buy:
    profit = sell - buy
    print('you made a profit', profit)
elif sell == buy:
    print('no profit no loss!')
else:
    loss = buy - sell
    print('you made a loss of' , loss)