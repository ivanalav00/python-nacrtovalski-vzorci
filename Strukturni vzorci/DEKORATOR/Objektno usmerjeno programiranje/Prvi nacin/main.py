#metoda, ki jo želimo "oviti"
def izracun_cene(cena_brez_popusta, popust):
    nova_cena = cena_brez_popusta - (cena_brez_popusta * (popust / 100))
    return nova_cena

#naš dekorator
def valuta(fn):

    #metoda za ovijanje
    def ovojnica(*args, **kwargs):
        #dobimo izračunano ceno s popustom
        cena = fn(*args, **kwargs)
        #vrnemo prilagojeno ceno
        return f'{cena}€'

    #vrnemo ovojnico
    return ovojnica

#ustvarimo konkreten dekorator
dekorator1 = valuta(izracun_cene)

#izpišemo ceno
print(dekorator1(20,10))





