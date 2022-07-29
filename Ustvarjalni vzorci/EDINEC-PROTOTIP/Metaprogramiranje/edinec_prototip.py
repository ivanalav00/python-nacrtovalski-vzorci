import copy

#meta-razred
class EdinecPrototipMetaPodatki(type):

    def __init__(cls, *args):
        #instanca ob inicializaciji ne obstaja
        cls.instance = None
        type.__init__(cls, *args)
        #ustvarimo razredno metodo kloniraj, ki klonira razred
        cls.kloniraj = lambda self: copy.deepcopy(self)

    #definiramo metodo za klicanje instance
    def __call__(cls, *args, **kwargs):
        #preverimo, če instanca obstaja
        if not cls.instance:
            #naredimo novo instanco s tem, da pokličemo metodo __call__ starševskega razreda
            cls.instance = type.__call__(cls, *args, **kwargs)
        #vrnemo instanco
        return cls.instance

#meta-razred uporabimo na razredu
class EdinecPrototip(metaclass=EdinecPrototipMetaPodatki):
    pass


