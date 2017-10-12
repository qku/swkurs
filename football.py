# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('D1s.csv')
data["Diff"] = abs(data.HTore - data.ATore)
data["Tore"] = data.HTore + data.ATore

print("Meiste Heimtore:")
print(data[data.HTore == data.HTore.max()])
print

print("Meiste Auswärtstore:")
print(data[data.ATore == data.ATore.max()])
print

print("Wenigste Heimtore:")
print(data[data.HTore == data.HTore.min()])
print

print("Größte Tordifferenz:")
print(data[data.Diff == data.Diff.max()])
print

#data.HTore[data.Heim == "Bayern Munich"].plot()
#plt.show()

#data.ATore[data.Auswaerts == "Bayern Munich"].plot()
#plt.show()

data.Tore.plot.hist()
plt.show()
