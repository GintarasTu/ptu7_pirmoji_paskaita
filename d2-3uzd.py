""""
leisti vartotojui po 1 įvesti 5 žodžius
pridėti įvestus žodžius į sąrašą
atspausdinti kiekvieną žodį, jo ilgį ir eilės numrį sąraše (nuo 1),
Sudėtingiau: kad programa leistų įvesti norimą žodžių kiekį
Patarimas: Naudoti sąrašą (list), ciklą for, funkcijas len ir index. enumerate (?)
"""
zodziai = []

for x in range(5):
    zodis = input("Iveskite zodi: ")
    zodziai.append(zodis)

skaitiklis = 0
for zodis in zodziai:
    skaitiklis += 1
    print(f"{skaitiklis}) - {zodis} ({len(zodis)})")
