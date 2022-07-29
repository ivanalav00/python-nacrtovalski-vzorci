class Edinec():

    #instanca na začetku ne obstaja
    instance = None

    #statična metoda, ki se kliče, ko se objekt ustvari
    def __new__(cls):
        #preverimo, če instanca obstaja
        if cls.instance == None:
            #ustvarimo novo instanco razreda
            cls.instance = object.__new__(cls)
        #vrnemo instanco
        return cls.instance

#ustvarimo razred, ki deduje od razreda Edinec
class EdinecOtrok(Edinec):
    pass


