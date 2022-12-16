"""
Perdaryti 5 užduoti taip, kad programa atspausdintų visus keliamuosius metus, nuo 1900 iki 2100 metų.

Keliamieji metai yra kas 4 metus, išskyrus paskutinius amžiaus metus, kurie keliamieji yra tik kas 400 metų

Patarimas: Google! :) ir f-ja isleep()
"""

metai = int(input("Įveskite metus YYYY formatu: "))

if (metai % 4 == 0 and metai % 100 != 0 or metai % 400 == 0):
    print("Keliamieji metai")
else:
    print("Metai yra nekeliamieji.")