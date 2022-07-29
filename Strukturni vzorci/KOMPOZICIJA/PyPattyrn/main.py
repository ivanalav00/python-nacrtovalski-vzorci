from komponente import *

slikaPocitnice1 = Datoteka("pocitnice1.jpg", 3)
slikaPocitnice2 = Datoteka("pocitnice2.jpg", 3)
slikaPocitnice3 = Datoteka("pocitnice3.jpg", 3)

slikaZivali1 = Datoteka("zivali1.jpg", 3)
slikaZivali2 = Datoteka("zivali2.jpg", 3)

slikaDruzinska = Datoteka("druzina.jpg", 3)

mapa_koren = Mapa(Datoteka)
mapa_pocitnice = Mapa(Datoteka)
mapa_zivali = Mapa(Datoteka)
mapa_druzinska = Mapa(Datoteka)

mapa_pocitnice.add_component(slikaPocitnice1)
mapa_pocitnice.add_component(slikaPocitnice2)
mapa_pocitnice.add_component(slikaPocitnice3)

mapa_zivali.add_component(slikaZivali1)
mapa_zivali.add_component(slikaZivali2)

mapa_druzinska.add_component(slikaDruzinska)

mapa_koren.add_component(mapa_pocitnice)
mapa_koren.add_component(mapa_zivali)
mapa_koren.add_component(mapa_druzinska)

print("Velikost slike: " + str(slikaPocitnice3.velikost()))
print("Velikost mape POČITNICE: " + str(mapa_pocitnice.velikost()))
print("Velikost mape SLIKE: " + str(mapa_koren.velikost()))


