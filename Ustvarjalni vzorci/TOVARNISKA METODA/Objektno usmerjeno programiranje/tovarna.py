from prevajalniki import *

#razred TovarnaPrevajalnikov za ustvarjanje drugih razredov
class TovarnaPrevajalnikov(object):

    #glede na željen jezik ustvarimo primeren prevajalnik
    @classmethod
    def ustvari(cls, jezik):
        if(jezik == "slovenscina"):
            return PrevajalnikSlovenscina()
        if(jezik == "nemscina"):
            return PrevajalnikNemscina()



