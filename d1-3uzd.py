zodis1 = str("helovynas")
print(zodis1.upper())
zodis2 = "HELOVYNAS"
print(zodis2.casefold())
print(zodis1.capitalize())
zodis3 = str("Hakuna Matata")
print(zodis3.count("a"))
print(zodis3.count("t"))
print(zodis3.find("H"))
print(zodis3.find("M"))
print(zodis3.center(100))
zodis4 = str("Barščiai")
print(zodis4.encode())
print(zodis4.encode(encoding="ascii",errors="replace"))
print(zodis4.encode(encoding="ascii",errors="namereplace"))
print(zodis4.encode(encoding="ascii",errors="ignore"))
print(zodis4.isascii())
print(zodis1.isascii())
zodis5 = "   tarpai.tarpeliai@gmail.com   "
print(zodis5.strip())
print(zodis5.strip(" @gmail.co"))
