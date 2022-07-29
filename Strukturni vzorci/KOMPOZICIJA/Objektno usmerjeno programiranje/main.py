from datoteka import Datoteka
from mapa import Mapa

mapaSlike = Mapa("SLIKE")

mapaPocitnice = Mapa("POČITNICE")
slikaPocitnice1 = Datoteka("pocitnice1.jpg", 3)
slikaPocitnice2 = Datoteka("pocitnice2.jpg", 3)
slikaPocitnice3 = Datoteka("pocitnice3.jpg", 3)

mapaZivali = Mapa("ŽIVALI")
slikaZivali1 = Datoteka("zivali1.jpg", 3)
slikaZivali2 = Datoteka("zivali2.jpg", 3)

mapaDruzina = Mapa("DRUŽINA")
slikaDruzinska = Datoteka("druzina.jpg", 3)

mapaSlike.dodaj(mapaPocitnice)
mapaSlike.dodaj(mapaZivali)
mapaSlike.dodaj(mapaDruzina)

mapaPocitnice.dodaj(slikaPocitnice1)
mapaPocitnice.dodaj(slikaPocitnice2)
mapaPocitnice.dodaj(slikaPocitnice3)
mapaZivali.dodaj(slikaZivali1)
mapaZivali.dodaj(slikaZivali2)
mapaDruzina.dodaj(slikaDruzinska)

print("Velikost slike: " + str(slikaPocitnice3.velikost()))
print("Velikost mape POČITNICE: " + str(mapaPocitnice.velikost()))
print("Velikost mape SLIKE: " + str(mapaSlike.velikost()))

print(slikaPocitnice3.lahko_sestavlja()) #False
print(mapaSlike.lahko_sestavlja()) #True
