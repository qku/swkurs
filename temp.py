# print Celsius->Fahrenheit Tabelle
lower = 0
upper = 300
step = 20

celsius = lower
while ( celsius < upper ):
    fahr = (celsius * 9./5) + 32
    print 'Celsius %6.1f = Fahrenheit %6.3f' % (celsius, fahr)
    celsius += step

