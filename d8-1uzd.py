"""
Sukurti programą, kuri:
Turėtų klasę Automobilis
Automobilis turėtų savybes: metai, modelis, kuro_tipas
Automobilis turėtų metodus: vaziuoti, stoveti, pildyti_degalu, kurie atitinkamai atspausdintų „Važiuoja“, „Priparkuota“, „Degalai įpilti“
Sukūrus objektą, automatiškai atspausdintų automobilio metus, modelį ir kuro tipą
Turėtų klasę Elektromobilis (jo tėvinis objektas – Automobilis)
Elektromobilis pakeistų Automobilio metodą pildyti_degalu taip, kad jis atspausdintų „Baterija įkrauta“
Elektromobilis turėtų metodą vaziuoti_autonomiskai, kuris spausdintų „Važiuoja autonomiškai“
Sukurti norimą Automobilio objektą
Sukurti norimą Elektromobilio objektą
Su sukurtu Automobilio objektu paleisti funkcijas vaziuoti, stoveti, pildyti_degalu
Su sukurtu Elektromobilio objektu paleisti funkcijas vaziuoti, stoveti, pildyti_degalu, vaziuoti_autonomiskai
"""
class Automobilis():

    def __init__(self, metai, modelis, kuro_tipas):
        self.metai = metai
        self.modelis = modelis
        self.kuro_tipas = kuro_tipas
        print(self.metai, self.modelis, self.kuro_tipas)

    def vaziuoti(self):
        print("Vaziuoja")

    def stoveti(self):
        print("Priparkuota")

    def pripildyti_degalu(self):
        print("Degalai įpilti")


automobilis1 = Automobilis(2010, "Renault Laguna", "benzinas")
automobilis1.vaziuoti()
automobilis1.stoveti()
automobilis1.pripildyti_degalu()
automobilis2 = Automobilis(1997, "Audi 100", "dyzelis")
automobilis2.vaziuoti()
automobilis2.stoveti()
automobilis2.pripildyti_degalu()


class Elektromobilis(Automobilis):

    def pripildyti_degalu(self):
        #super().pripildyti_degalu() - nereikalinga, nes perima tėvinės klasės savybę
        print("Baterija įkrauta")

    def vaziuoti(self):
        print("Važiuoja autonomiškai")

elektromobilis = Elektromobilis(2022, "Nissan Leaf", "elektromobilis")
elektromobilis.vaziuoti()
elektromobilis.stoveti()
elektromobilis.pripildyti_degalu()
