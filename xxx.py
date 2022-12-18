eil_nr = 1
produktas = "KAva"
produktas = produktas.replace('KAva', 'kavos')
produkto_rusis = "Lavazza"
pakuociu_kiekis = 5
kaina = 8.99
uzsakymo_suma = pakuociu_kiekis * kaina
mano_uzsakymas = 'Mano uzsakymas nr. {}. Užsakau {} pakuotes {} {}, kainuojančias {}. \nUž "viską" sumokėsiu {}.'
print(mano_uzsakymas.format(eil_nr, pakuociu_kiekis, produktas, produkto_rusis, kaina, uzsakymo_suma))

