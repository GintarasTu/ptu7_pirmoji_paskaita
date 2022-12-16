skaičius1 = int(input("Įveskite pirmąjį skaičių: "))
skaičius2 = int(input("Įveskite antrąjį skaičių: "))
skaičius3 = int(input("Įveskite trečiąjį skaičių: "))
if skaičius1 >= 10:
    print(skaičius2 + skaičius3)
if skaičius1 < 8:
    print(skaičius3 - skaičius2)
else:
    print(skaičius3 // skaičius2)
    # kodėl neveikia % eilutėje su 'print'?
    # sveikąją dalį nurodo '//', liekaną - '%'

