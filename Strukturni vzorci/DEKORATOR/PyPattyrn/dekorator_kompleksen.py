from pypattyrn.structural.decorator import DecoratorComplex, CallWrapper

#kompleksen Dekorator, ki prejme argument
class Kompleksna_Valuta(DecoratorComplex):

    #pri inicializaciji kot argument dobimo znak
    def __init__(self, znak):
       self.znak = znak

    #funkcijski dekorator za ovijanje
    @CallWrapper
    def __call__(self, func, *args, **kwargs):
        cena = func(*args, **kwargs)
        return f'{cena}{self.znak}'


class Kompleksen_Izracun(object):

    #funkcijski dekorator, ki nakazuje Dekorator in mu doda inicializacijski argument
    @Kompleksna_Valuta('€')
    def izracun_cene(self, cena_brez_popusta, popust):
        nova_cena = cena_brez_popusta - (cena_brez_popusta * (popust / 100))
        return nova_cena


