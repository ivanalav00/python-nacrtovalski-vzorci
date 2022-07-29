class ObiskovalecKosare(object):

    def obisci(self, parameter, *args):
        #pridobimo ime tipa parametra
        ime_tipa = type(parameter).__name__.lower()
        #s pomočjo imena tipa poiščemo ime metode
        ime_metode = "obisci_" + ime_tipa
        #sestavimo metodo
        metoda = getattr(self, ime_metode)
        #pokličemo in vrnemo ustvarjeno metodo
        return metoda(parameter, *args)

    def obisci_sadje(self, sadje, *args):
        cena = sadje.teza * sadje.cenaNaKg
        # pogledamo, če je bil vnesen popust
        if (len(args) >= 1):
            popust = args[0]
            return cena - (cena * (popust / 100))
        else:
            return cena

    def obisci_knjiga(self, knjiga, *args):
        return knjiga.cena