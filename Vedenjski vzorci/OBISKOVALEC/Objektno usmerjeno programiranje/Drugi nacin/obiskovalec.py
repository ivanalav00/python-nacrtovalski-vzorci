from  izdelki import *
from main import obiskovalecDekorator

class ObiskovalecKosare:
    @obiskovalecDekorator(Sadje)
    def obisci(self, sadje):
        return sadje.teza * sadje.cenaNaKg

    @obiskovalecDekorator(Knjiga)
    def obisci(self, knjiga):
        return knjiga.cena