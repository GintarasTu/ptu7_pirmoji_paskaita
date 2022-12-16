"""
Sukurkite ir išsibandykite funkcijas, kurios:
1 Gražinama trijų paduotų skaičių suma.
2 Gražintų paduoto sąrašo iš skaičių, sumą.
3 Atspausdintų didžiausią iš kelių paduotų skaičių (panaudojant *args).
4 Gražintų paduotą stringą atbulai.
5 Atspausdintų, kiek paduotame stringe yra žodžių, didžiųjų ir mažųjų raidžių, skaičių.
6 Gražintų sąrašą tik su unikaliais paduoto sąrašo elementais.
7 Gražintų, ar paduotas skaičius yra pirminis.
8 Išrikiuotų paduoto stringo žodžius nuo paskutinio iki pirmojo
9 Gražina, ar paduoti metai yra keliamieji, ar ne.
10 Atspausdina, kiek nuo paduotos sukakties praėjo metų, mėnesių, dienų, valandų, minučių, sekundžių.
"""
"""
1 Gražinama trijų paduotų skaičių suma.
"""
def susumuojam (skaicius1, skaicius2, skaicius3):
    # suma = skaicius1 + skaicius2 + skaicius3
    return skaicius1 + skaicius2 + skaicius3
print("1. Trijų duotų skaičių suma: ", susumuojam(10, 21, 333))
"""
2. Gražinama paduoto sąrašo iš skaičių suma.
"""
def saraso_suma(sarasas):
    suma = 0
    for skaicius in sarasas:
        suma += skaicius
    return suma

sarasas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("2. Sąraše esančių skaičių suma yra: ", saraso_suma(sarasas))

"""
3 Atspausdinamas didžiausias sąrašo skaičius (panaudojant *args).
"""
def didziausias_skaicius(*sarasas):

    didziausias = 0
    for skaicius in sarasas:
        skaicius > didziausias
        didziausias = skaicius
    return (didziausias)
print(didziausias_skaicius())  #???

sarasas = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

