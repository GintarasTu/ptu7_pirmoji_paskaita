eil_nr = 1
produktas = "KAva"
produktas = produktas.replace('KAva', 'kavos')
produkto_rusis = "Lavazza"
pakuociu_kiekis = 5
kaina = 8.99
uzsakymo_suma = pakuociu_kiekis * kaina
mano_uzsakymas = 'Mano uzsakymas nr. {}. Užsakau {} pakuotes {} {}, kainuojančias po {}€. \nUž "viską" sumokėsiu {}€.'
print(mano_uzsakymas.format(eil_nr, pakuociu_kiekis, produktas, produkto_rusis, kaina, uzsakymo_suma))

Automobilis = "Citroen C4 Grand Picasso"
Pagaminimo_metai = 2010
Lizingo_imoka = 300
Palukanos = 3.5
Priskaiciuotos_palukanos = round((Lizingo_imoka * Palukanos * 3.5 / 100 / 12), 2)
Bendra_imokos_suma = (Lizingo_imoka + Priskaiciuotos_palukanos)
txt = '\nLizingo įmoka už {} {} m. - {}€. \nPriskaičiuotos palūkanos - {}€. \nBendra įmokos suma: {}€.'
print(txt.format(Automobilis, Pagaminimo_metai, Lizingo_imoka, Priskaiciuotos_palukanos, Bendra_imokos_suma))