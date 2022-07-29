from dekorator_preprost import *
from dekorator_kompleksen import *

#uporaba preprostega dekoratorja
izpis = Izracun()
print(izpis.izracun_cene(20,10))

#uporaba kompleksnega dekoratorja
kompleksen_izpis = Kompleksen_Izracun()
print(kompleksen_izpis.izracun_cene(20,10))

