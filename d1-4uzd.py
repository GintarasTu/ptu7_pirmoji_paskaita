a = int(input("Įveskite pirmą skaičių: "))
b = int(input("Įveskite antrą skaičių: "))
c = float(input("Įveskite trečią skaičių: "))

# kodėl neatlieka veiksmo su nesveikuoju skaičiumi?

if(a == b):
    print("Skaičių sandauga: ", a * b * c)
elif(a > b):
    print("Skaičių skirtumas: ", a - b)
else:
# importuojame biblioteką šaknies traukimui
    import math
    print("Šaknis iš trečiojo skaičiaus: ", math.sqrt(c))
# iš paskaitos, liko nebaigta
# a = float(input("Įveskite pirmą skaičių: "))
# b = float(input("Įveskite antrą skaičių: "))
# veiksmas = (input("Įveskite veiksmą (+,-,*,/): "))