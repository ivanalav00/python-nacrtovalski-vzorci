from pypattyrn.behavioral.iterator import Iterator

class PregledovalnikSodihStevil(Iterator):

    #pripravimo prvo in zadnje število
    def __init__(self, prvo_stevilo, zadnje_stevilo):
        self.trenutno_stevilo = prvo_stevilo
        self.zadnje_stevilo = zadnje_stevilo

    # definiramo metodo vračanje naslednjega elementa
    def __next__(self):
        return self.izracun()

    #definiramo metodo, ki implementira logiko za vračanje sodih elementov
    def izracun(self):
        stevilo = self.trenutno_stevilo

        #ustvarimo zanko
        while True:
            #preverimo če je število sodo
            if stevilo % 2 == 0:
                return stevilo

            #povečamo število
            stevilo = self.trenutno_stevilo
            self.trenutno_stevilo += 1

            #vprašamo, če je zadnje število večje od nič in če je manjše od trenutnega števila
            if self.zadnje_stevilo > 0 and self.trenutno_stevilo > self.zadnje_stevilo+1:
                #končamo iteracijo
                raise StopIteration




