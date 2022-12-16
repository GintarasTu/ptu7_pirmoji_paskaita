"""
Sukurti programą, kuri:
Turėtų klasę Darbuotojas
Darbuotojas turėtų savybes: vardas, valandos_ikainis, dirba_nuo
Turėtų privatų metodą kuris paskaičiuotų, kiek darbuotojas nudirbo dienų nuo įvestos dienos (dirba_nuo) iki šiandien (turint omeny, kad darbuotojas dirba 7 dienas per savaitę)
Turėtų metodą paskaiciuoti_atlyginima, kuris panaudodamas aukščiau aprašytu metodu, paskaičiuotų bendrą atlyginimą (turint omeny, kad darbuotojas dirba 8 valandas per dieną)
Turėtų klasę NormalusDarbuotojas, kuri pakeistų Darbuotojo klasę taip, kad ji skaičiuotų atlyginimą, dirbant darbuotojui 5 dienas per savaitę
Sukurti norimą Darbuotojo objektą
Sukurti norimą NormalusDarbuotojas objektą
Su abiem objektais paleisti funkciją paskaiciuoti_atlyginima
"""
import datetime
siandien = datetime.datetime.today()

class Darbuotojas:

    def __init__(self, vardas, valandos_ikainis, dirba_nuo):
        self.vardas = vardas
        self.valandos_ikainis = valandos_ikainis
        self.dirba_nuo = datetime.datetime.strptime(dirba_nuo, "%Y-%m-%d")

    def dienu_skirtumas(self):
        skirtumas = siandien - self.dirba_nuo
        print(skirtumas.days)
        return skirtumas.days # grąžinamas skirtumas dienomis, kad kitas objektas galėtų jį naudoti

    def atlyginimas(self):
        uzdarbis = self.valandos_ikainis * 8 * darbuotojas.dienu_skirtumas()
        print(uzdarbis)

class NormalusDarbuotojas(Darbuotojas):

    def atlyginimas(self):
        normalus_atlyginimas = int((darbuotojas.dienu_skirtumas() / 7 * 5 + dienu_liekana) * 8 * self.valandos_ikainis)
        print(normalus_atlyginimas)
        #return normalus_atlyginimas

darbuotojas = Darbuotojas("Gintaras Tumas", 8, "2020-08-01")
darbuotojas.dienu_skirtumas()
darbuotojas.atlyginimas()
normalus_darbuotojas = NormalusDarbuotojas("Gintaras Tumas", 8, "2020-08-01")
dirbta_savaiciu = darbuotojas.dienu_skirtumas() / 7
dienu_liekana = darbuotojas.dienu_skirtumas() - (dirbta_savaiciu * 7)
normalus_darbuotojas.atlyginimas()
