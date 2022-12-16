# atspausdinti norimą sąrašą ir žodyną, ir juose:
# - atsp. 1 norimą įrašą
# - pridėti įrašą
# - ištrinti įrašą
# - pakeisti įrašą

sarasas = ["Code", "Academy", "paskaita"]
print(sarasas)
print(sarasas[1])

sarasas.append("Python")
print(sarasas)
# ar galima nurodyti konkrečią įterpimo vietą? galima, su f-ja 'insert'
sarasas.insert(2, "Python")
sarasas.pop(4)
sarasas[0] = "Science"
print(sarasas)

sarasas.pop(2)
print(sarasas)

zodynas = {"Ledai": "vyšniniai", "Sultys": "obuolių", "Saldainiai": "mėtiniai"}
print(zodynas), (zodynas["Sultys"]), (zodynas["Ledai"])
zodynas["Sausainiai"] = 'imbieriniai'
print(zodynas)
del zodynas["Ledai"]
print(zodynas)
zodynas["Sausainiai"] = 'kakaviniai'
print(zodynas), ("Programos pabaiga")