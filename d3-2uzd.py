"""
Parašyti programą, kuri:

Atspausdintų dabartinę datą ir laiką
Atimtų iš dabartinės datos ir laiko 5 dienas ir juos atspausdintų
Pridėti prie dabartinės datos ir laiko 8 valandas ir juos atspausdintų
Atspausdintų dabartinę datą ir laiką tokiu formatu: 2019 03 08, 09:57:17
Patarimas: naudoti datetime, timedelta (from datetime import timedelta)
"""

import datetime

print(datetime.datetime.today())
x = datetime.datetime.today()
print("Data ir laikas dabar: ", x)

dabar = datetime.datetime.now()
print("Data prieš penkias dienas: ", dabar - datetime.timedelta(days=5))
print("Laikas po 8 valandų: ", dabar + datetime.timedelta(hours=8))
print("Data ir laikas kitokiu formatu: ", dabar.strftime("%Y %m %d, %X"))