""""
Sukurti programą, kuri:
Sukurtų failą „Tekstas.txt“ su pilnu tekstu, gauto python kode paleidus „import this“.
Atspausdintų tekstą iš sukurto failo
Paskutinėje sukurto failo eilutėje pridėtų šiandienos datą ir laiką
Sunumeruotų teksto eilutes (kiekvienos pradžioje pridėtų skaičių).
Sukurtame faile eilutę "Beautiful is better than ugly." pakeistų į "Gražu yra geriau nei bjauru."
Atspausdintų visą failo tekstą atbulai
Atspausdintų, kiek failo tekste yra žodžių, skaičių, didžiųjų ir mažųjų raidžių
Nukopijuotų visą sukurto failo tekstą į naują failą, tik DIDŽIOSIOMIS RAIDĖMIS
Patarimai:
Naudoti from datetime import datetime, datetime.today()
Kintamajam priskirti sakinį, kuriuo bus operuojama, eilutėmis
Kai kur galima panaudoti funkcijas iš praeitų pamokų
"""
import datetime
data_laikas = datetime.datetime.today()
eil_nr = 0

with open("failas.txt", 'w', encoding="utf-8") as failas:           #sukuriamas failas
    failas.write("Failų kūrimo pamoka, įrašant duomenis į failą.\n Beautiful is better than ugly. \n")  #įrašant tekstą
with open("failas.txt", 'r', encoding="utf-8") as failas:           #atspausdinamas įvestas tekstas
    print(failas.read())
with open("failas.txt", 'w', encoding="utf-8") as failas:           #sukuriamas failas
    failas.write("Failų kūrimo pamoka, įrašant duomenis į failą.\n Gražu yra geriau nei bjauru. \n")  #perrašytas antras sakinys
with open("failas.txt", 'a', encoding="utf-8") as failas:
    failas.write("Failas papildytas nauju sakiniu. \n")                #įrašomas papildomas sakinys


with open("failas.txt", 'a', encoding="utf-8") as failas:
    failas.write(str(datetime.datetime.today()))                    #pridėta data, var. 1
with open("failas.txt", 'r', encoding="utf-8") as failas:
     print(failas.read(), "\n", data_laikas.strftime("%Y-%m-%d %X"))       #pridėta data, var. 2

with open("failas.txt", 'w', encoding="utf-8") as failas:           #sukuriamas failas
    failas.write("Failų kūrimo pamoka, įrašant duomenis į failą.\n Beautiful is better than ugly. \n")  #įrašant tekstą
with open("failas.txt", 'r', encoding="utf-8") as failas:           #atspausdinamas įvestas tekstas
    print(failas.read()[::-1])                                      #tekstas spausdinamas atbulai

