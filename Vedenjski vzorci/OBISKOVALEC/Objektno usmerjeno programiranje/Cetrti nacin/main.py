from decimal import Decimal
from functools import singledispatch
from  izdelki import *

@singledispatch
def obisci(parameter):
   pass

@obisci.register(Sadje)
def obisci1(sadje):
    return sadje.teza * sadje.cenaNaKg

@obisci.register(Knjiga)
def obisci2(knjiga):
    return knjiga.cena

@obisci.register(Decimal)
@obisci.register(int)
def obisci3(popust, sadje):
    cena = sadje.teza * sadje.cenaNaKg
    return cena - (cena * (popust/100))

print(obisci(15, Sadje(12,3)))
print(obisci(Sadje(12,3)))
print(obisci(Knjiga(12)))

