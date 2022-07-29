class Komponenta(object):

    def do_something(self):
        pass


class Datoteka(Komponenta):

    def __init__(self, ime, velikost):
        self.did_something = False

    def do_something(self):
        self.did_something = True

