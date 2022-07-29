from pypattyrn.creational.factory import Factory
from prevajalniki import *

class TovarnaPrevajalnikov(Factory):

    #glede na željen jezik ustvarimo primeren prevajalnik
    @classmethod
    def ustvari(cls, jezik):
        if(jezik == "slovenscina"):
            return PrevajalnikSlovenscina()
        if(jezik == "nemscina"):
            return PrevajalnikNemscina()

