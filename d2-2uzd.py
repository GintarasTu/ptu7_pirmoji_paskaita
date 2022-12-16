# - leisti vartotojui įvesti skaičių
# - jei įvestas skaičius yra teigiamas, paprašyti įvesti dar 1 skaičių
# - jei į vestas skaičius yra neigiamas, nutraukti programą ir atspausdinti visų įvestų teigiamų skaičių sumą
#  - while, if, break

suma = 0
a = 0
while a >= 0:
    suma += a
    a = int(input("Įveskite skaičių: "))
    continue

print(suma)
print("Programos pabaiga")
