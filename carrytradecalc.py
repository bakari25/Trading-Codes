print('How many years will you be investing for?')
years = int(input('Enter Years: '))

print('How much money is in your account?')
principal = float(input('Enter current amount in account: '))

print('How much money do you plan on paying monthly for loan?')
monthly_payment = float(input('Enter amount: '))

print('What do you estimate will be the yearly interest of this investment?')
interest = float(input('Enter interest in decimal numbers (10% = 0.1): '))

print('What do you estimate will be the yearly interest of the loan for investment?')
interestl = float(input('Enter interest in decimal numbers (10% = 0.1): '))

monthly_payment = monthly_payment * 12
invest_amount = 0
loanamount=0

for i in range(0, years):
    if invest_amount == 0:
        invest_amount = principal
    if loanamount ==0:
        loanamount = principal
    loanamount=((loanamount-monthly_payment)*(1+interestl))+monthly_payment
    invest_amount = (invest_amount) * (1+interest)

loancost=loanamount-principal
investac=invest_amount-principal
totalprofit=investac-loancost
print('Investment account profits after period:',round(investac,2))
print('Loan cost over period:',round(loancost,2))
print('Net profit overtime:',round(totalprofit,2))
