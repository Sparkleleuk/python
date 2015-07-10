import EURtoUSD
for euro in (5, 21, 35):
    print 'EUR ' + str(euro) + ' = USD ' + str(EURtoUSD.EURtoUSD(euro))

    print 'EUR {} = USD {}'.format(euro, EURtoUSD.EURtoUSD(euro))
print 'done'   