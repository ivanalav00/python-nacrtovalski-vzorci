from functools import wraps

def valuta(fn):
    #dodamo funkcijski dekorator, ki pokaže katera funckija je ovojnica
    @wraps(fn)
    def ovojnica(*args, **kwargs):
        cena = fn(*args, **kwargs)
        return f'{cena}€'

    return ovojnica

#dodamo funkcijski dekorator, ki pove katera metoda je dekorator
@valuta
def izracun_cene(cena_brez_popusta, popust):
    nova_cena = cena_brez_popusta - (cena_brez_popusta * (popust / 100))
    return nova_cena


#lahko pokličemo le izracun_cene, ker se dekorator že kliče
#v funckijskem dekoratorju
print(izracun_cene(20,10))



