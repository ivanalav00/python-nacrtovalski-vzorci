import copy

#meta-razred za prototip
class PrototipMetaPodatki(type):

    #ustvarimo razredno metodo kloniraj, ki klonira razred
    def __init__(cls, *args):
        type.__init__(cls, *args)
        cls.kloniraj = lambda self: copy.deepcopy(self)

#meta-razred uporabimo na razredu Prototip
class Prototip(metaclass=PrototipMetaPodatki):
    pass


