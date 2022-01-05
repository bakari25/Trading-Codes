#backtesting win and loss calculator
acbal=float(input('how much is account balance?'))
print('initial account balance is',acbal)
maxloss=float(input('What is your max risk in %(in dec.) of account per trade?'))
#max loss per trade
while True:
    WorL=input('Was trade a win, loss, or break even?')
    if WorL == 'win':
        r=float(input('trade win to loss ratio in integer:'))
        profit=r*(maxloss*acbal)
        acbal=acbal+profit
        print('New account balance',acbal)
        continue
    if WorL == 'loss':
        loss=(acbal*maxloss)
        acbal=acbal-loss
        print('New account balance',acbal)
        continue
    if WorL == 'break even':
         continue
    if WorL == 'done':
         break
finalbal=int(acbal)
print('final account balance:',finalbal)
