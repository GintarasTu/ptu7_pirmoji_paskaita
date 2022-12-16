"""
Pakeisti 1 užduotį taip, kad neteisingai įvedus duomenis ar įvykus klaidoms,
 programos mestų norimas klaidas lietuvių kalba (panaudoti try/except)
"""
    # ValueError: invalid literal for int()
while True:
    try:
        x = int(input("Įveskite sveiką skaičių: "))
        break
    except ValueError:
        print("Įvestas neteisingo formato skaičius (nesveikas :))")
        print("Bandykite dar kartą.")
print(x > 0)