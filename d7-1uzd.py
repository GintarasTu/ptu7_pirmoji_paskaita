""""
Parašyti klasę Sakinys, kuri turi savybę tekstas ir metodus, kurie:
Gražina tekstą atbulai
Gražina tekstą mažosiomis raidėmis
Gražina tekstą didžiosiomis raidėmis
Gražina žodį pagal nurodytą eilės numerį
Gražina, kiek tekste yra nurodytų simbolių arba žodžių
Gražina tekstą su pakeistu nurodytu žodžiu arba simboliu
Atspausdina, kiek sakinyje yra žodžių, skaičių, didžiųjų ir mažųjų raidžių
Susikurti kelis klasės objektus ir išbandyti visus metodus
"""

class Sakinys:
    def __init__(self, zodis1, zodis2, zodis3):
        self.zodis1 = zodis1
        self.zodis2 = zodis2
        self.zodis3 = zodis3


    def atbulai(self):
        return self.zodis1[::-1], self.zodis2[::-1], self.zodis3[::-1]

    def mazosiomis(self):
        return self.zodis1.lower()

    def didziosiomis(self):
        return self.zodis1.upper(), self.zodis2.upper(), self.zodis3.upper()

    def simboliu_skaicius(self):
        kiek_skaiciu self.len([x for x in self.zodis1 if x.isdigit()])


sakinys1 = Sakinys("Objektinio", "programavimo", "principai.")
sakinys2 = Sakinys("Sukuriama", "objekto", "klasė.")

print(sakinys1.atbulai())
print(sakinys1.mazosiomis())
print(sakinys1.didziosiomis())
print(sakinys1.kiek_skaiciu())
print((sakinys1.zodis1, sakinys1.zodis2, sakinys1.zodis3)[::-1])
print(sakinys2.zodis1, sakinys2.zodis2, sakinys2.zodis3)