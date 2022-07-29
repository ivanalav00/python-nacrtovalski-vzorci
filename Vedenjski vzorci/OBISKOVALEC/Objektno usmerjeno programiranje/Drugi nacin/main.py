from obiskovalec import ObiskovalecKosare
from  izdelki import *

#vrnemo popolnoma kvalificirano ime objekta
def kvalificiranoIme(obj):
    return obj.__module__ + '.' + obj.__qualname__

#pridobi ime razreda, ki je deklariralo objekt
def razred(obj):
    ime = kvalificiranoIme(obj)
    return ime[:ime.rfind('.')]

#vse metode obiskovalca
metode = {}

#implementacija obiskovalca - vrnemo primerno metodo
def obiskovalec(self, arg):
    metoda = metode[(kvalificiranoIme(type(self)), type(arg))]
    return metoda(self, arg)

#dekorator za obiskovalca
def obiskovalecDekorator(tip_argumenta):
    def dekorator(fn):
        zeljen_razred = razred(fn)
        metode[(zeljen_razred, tip_argumenta)] = fn
        return obiskovalec
    return dekorator


obiskovalec = ObiskovalecKosare()
print(obiskovalec.obisci(Sadje(12, 3)))
print(obiskovalec.obisci(Knjiga(12)))

