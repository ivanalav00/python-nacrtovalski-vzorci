from obiskovalec import ObiskovalecKosare
from  izdelki import *

#definiramo metodo, ki jo bomo klicali za vse primere
@ObiskovalecKosare
def obisci(x):
    pass

#naredimo primer metode za razred Sadje
@obisci.primer(Sadje)
def obisci1(sadje):
    return sadje.teza * sadje.cenaNaKg

#naredimo primer metode za razred Knjiga
@obisci.primer(Knjiga)
def obisci2(knjiga):
    return knjiga.cena

#kličemo metode
print(obisci(Sadje(12, 3)))
print(obisci(Knjiga(12)))

