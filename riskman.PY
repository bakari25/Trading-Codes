#risk mamagement code

accountbalance=None
risk=0.03
slpips=None
while True:
    accountbalance=input('What is current account/portfolio balace?')
    slpips=input('how man pips from entry to sl?')
    actb=float(accountbalance)
    r=float(risk)
    sp=int(slpips)
    lotsize=(actb*r)/sp
    ls=float(lotsize)
    print('For proper risk management use:',ls)
    tradedec=input('Was trade executed?')
    if tradedec == 'no':
        continue
    elif tradedec == 'yes':
        takeprofit=input('How many pips is takeprofit?')
        tp=int(takeprofit)
        profit=tp*ls
        rr=tp/sp
        break
print('risk/reward ratio:',rr)
print('profit:',profit)
