#obiskovalec
class ObiskovalecKosare(object):
    #s funkcijo omogočimo, da uporabimo razred kot funkcijski dekorator
    def __init__(self, funkcija):
        self.funkcija = funkcija
        #primeri vseh funkcij obisci
        self.primeri = {}

    #definiramo metodo primer, ki v primere metod doda novo metodo
    def primer(self, izdelek):
        def poklici(fun):
            self.primeri[(izdelek)] = fun
        return poklici

    #omogočimo, da se razred lahko kliče in da vrne metodo s primernimi argumenti
    def __call__(self, arg):
        fun = self.primeri[type(arg)]
        return fun(arg)
