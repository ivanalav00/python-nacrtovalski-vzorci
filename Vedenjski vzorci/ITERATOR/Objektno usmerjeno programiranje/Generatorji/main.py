#generator za pregledovanje sodih števil
def generator(razpon):
    #prvo število bo enako prvemu številu v razponu
    stevilo = razpon.start
    #pregledujemo števila do zadnjega v razponu
    while stevilo <= razpon.stop:
        #preverimo, če je število sodo
        if stevilo % 2 == 0:
            #sodo število vrnemo
            yield stevilo
        #število povečamo
        stevilo += razpon.step

for st in generator(range(1, 21)):
    print(st)
