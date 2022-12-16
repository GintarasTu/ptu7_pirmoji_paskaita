""""
Parašyti programą, kuri:
    Leistų vartotojui įvesti norimą datą ir laiką (pvz. gimtadienį)
    Paskaičiuotų ir atspausdintų, kiek nuo įvestos datos ir laiko praėjo:
        Metų
        Mėnesių
        Dienų
        Valandų
        Minučių
        Sekundžių
Kadangi tiksliai galima paskaičiuoti tik dienas ir sekundes, metus, mėnesius ir t.t. paskaičiuokite apytiksliai.
Patarimas: naudoti datetime, .days, .total_seconds()

Skaičių suapvalinimo pavyzdys (kurio gali prireikti šioje užduotyje):
skaicius = 4.66
print(round(skaicius))
1968-03-16
"""
import datetime
dabar = datetime.datetime.now()
ivesta_data = (input("Įveskite datą: (YYYY-MM-DD formatu) "))
data = datetime.datetime.strptime(ivesta_data, "%Y-%m-%d")
skirtumas = dabar - data
# print(skirtumas.days)
print("Jūsų amžius metais:     ", int(skirtumas.days / 365))
print("            mėnesiais:  ", int(skirtumas.days / 365 * 12))
print("            dienomis:   ", int(skirtumas.days))
print("            valandomis: ", int(skirtumas.days * 24))
print("            minutėmis:  ", int(skirtumas.days * 24 * 60))
print("            sekundėmis: ", int(skirtumas.days * 24 * 3600))
print("Programos pabaiga")