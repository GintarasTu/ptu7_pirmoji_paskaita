"""
Parašyti programą, kuri:
Leistų vartotojui įvesti sveiką skaičių.
Atspausdinti True, jei skaičius teigiamas
Atspausdinti False, jei skaičius neigiamas ar lygus 0
True/False reikšmei išsaugoti naudoti boolean tipo kintamąjį ar_skaicius_teigiamas
Patarimas: naudoti input, boolean, if/else

"""
x = int(input("Įveskite sveiką skaičių: "))
if x > 0:
    print(x > 0)
else:
    print("False")