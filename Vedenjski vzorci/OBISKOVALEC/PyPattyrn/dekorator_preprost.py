from pypattyrn.structural.decorator import DecoratorSimple

#razred, ki bo deloval kot preprost Dekorator
class Valuta(DecoratorSimple):

    #izracunano ceno vrnemo skupaj z znakom za euro
    def __call__(self, *args, **kwargs):
        cena = self.func(*args, **kwargs)
        return f'{cena}€'

#razred, ki ga Dekorator ovije
class Izracun(object):

    #funckijski dekorator, ki pokaže, kateri razred je naš Dekorator
    @Valuta
    def izracun_cene(self, cena_brez_popusta, popust):
        nova_cena = cena_brez_popusta - (cena_brez_popusta * (popust / 100))
        return nova_cena


