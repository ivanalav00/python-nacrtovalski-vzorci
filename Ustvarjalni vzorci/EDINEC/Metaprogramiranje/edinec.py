#ustvarimo meta-razred
class EdinecMetaPodatki(type):

    #definiramo metodo za inicalizacijo objekta
    def __init__(cls, *args):
        cls.instance = None

    # definiramo metodo za klicanje instance
    def __call__(cls, *args, **kwargs):
        #preverimo, če instanca obstaja
        if not cls.instance:
            #naredimo novo instanco s tem, da pokličemo metodo __call__ starševskega razreda
            cls.instance = type.__call__(cls, *args, **kwargs)
        #vrnemo instanco
        return cls.instance

#uporabimo meta-razred na dejanskem razredu
class EdinecMeta(metaclass=EdinecMetaPodatki):
    pass


