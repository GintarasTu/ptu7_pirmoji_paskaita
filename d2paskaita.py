# List tipo masyvas
sarasas = [4, 5, 8, 9]
zodziai = ["Labas", "diena", "rytas"]
kratinys = [4, 15, 3.5, "zodis", [5, 8, 9]]
print(zodziai[1][:4])
print(zodziai[0][2:4])
print(kratinys[4][1])

sarasas.append(55)
print(sarasas)
kratinys.append("naktis")
print(kratinys)

sarasas.insert(2, "tragedija")
print(sarasas)

sarasas.pop(3)
print(sarasas)
print(len(sarasas))
ilgas_zodis = "kilimandzaras"
print(len(ilgas_zodis))

# Dictionary tipo masyvas
# Dictionary neturi indekso (0,1,2), "Rokas" yra raktas
amzius = {"Rokas": 20, "Andrius": 25, "Laura": 28}
# amzius["Donatas"]: 99 kažkas ne taip
print(amzius)
print(amzius["Andrius"])

# Ciklai
sarasas2 = [4, 5, 56, 45, 78, 45, 152]

for kvadratas in sarasas2:
    print(kvadratas ** 2)

# for kvadratu in sarasas2:
#     kvadratu.append(laipsnis ** 2)
#     print(laipsnis)

for raktas, reiksme in amzius.items():
    print(raktas, reiksme)

for x in range(4):
    print(x, "pavyko")

masyvas = list(range(5, 50, 5))
print(masyvas)

# tuple masyvas - neredaguojamas
# set masyvas - išrenkamos tik unikalios reikšmės

a = 25
while a < 99:
    a +=15
    print(a)