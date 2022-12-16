"""
Pakeisti 3 užduotį taip, kad neteisingai įvedus duomenis ar įvykus klaidoms,
 programos mestų norimas klaidas lietuvių kalba (panaudoti try/except)
"""
import datetime
dabar = datetime.datetime.now()

while True:
    try:
        ivesta_data = (input("Įveskite datą YYYY-MM-DD formatu: "))
        data = datetime.datetime.strptime(ivesta_data, "%Y-%m-%d")
        break
    except ValueError as klaida:
        print("Neteisingai įvesta data. Bandykite dar kartą.")
        print(klaida)

skirtumas = dabar - data
# print(skirtumas.days)
print("Jūsų amžius metais:     ", int(skirtumas.days / 365))
print("            mėnesiais:  ", int(skirtumas.days / 365 * 12))
print("            dienomis:   ", int(skirtumas.days))
print("            valandomis: ", int(skirtumas.days * 24))
print("            minutėmis:  ", int(skirtumas.days * 24 * 60))
print("            sekundėmis: ", int(skirtumas.days * 24 * 3600))
print("Programos pabaiga")