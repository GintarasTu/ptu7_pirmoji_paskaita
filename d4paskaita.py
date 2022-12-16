
# def pasisveikinimas(vardas):
#     print("Labas,", vardas)
#
# pasisveikinimas("Juozai,")
# pasisveikinimas("Petrai,")
# pasisveikinimas("Maryte,")

# def kvadratas(skaicius):
#     kvadratu = skaicius ** 2
#     print(kvadratu)
#     return (kvadratu) # return reikalingas reikšmei išvesti
#
# kvadratas (3)
# kvadratas(4)

# def skaiciu_suma (skaicius1, skaicius2, skaicius3=1):
#     suma = skaicius1 + skaicius2
#     rezultatas = suma * skaicius3
#     return rezultatas
# print(skaiciu_suma(5, 6, 12))
# print(skaiciu_suma(2, 2, 1))
# print(skaiciu_suma(3, 3))
#
# def skaiciu_suma (skaicius1=2, skaicius2=2, skaicius3=1):
#     suma = skaicius1 + skaicius2
#     rezultatas = suma * skaicius3
#     return rezultatas
# print(skaiciu_suma(5, 6, 12))
# print(skaiciu_suma(2, 2))
# print(skaiciu_suma(3))
# print(skaiciu_suma())

def kvadratai(*args): # * reiskia neribotus argumentus (list tipo masyvas)
    for skaicius in args:
        print(skaicius ** 2)
kvadratai(4, 5, 6, 8) # <- neribojami argumentai
kvadratai(3)
kvadratai() # nera reiksmes, nera ir atsakymo
#
# def spausdinti(**kwargs): # * zodyno tipo masyvas (raktas:reiksme)
#     for x in kwargs.items():
#         print(x)
#     #    return kwargs
#
# spausdinti(vardas="Adomas", amzius_metais=12)

# def suma(a, b):
# """  # padeda apra6yti parametrų reikšmes, ir jos pateikiamos
#  užvedus pelę ant f-jos pavadinimo
# :param a: skaičius a
# :param b: skaicius b
# :return:  grąžinamas atsakymas
# """
#     return a + b
#
# import calendar
# print(calendar)