from prevajalnik import Prevajalnik

#ustvarimo podrazred PrevajalnikSlovenscina, ki deduje od razreda Prevajalnik
class PrevajalnikSlovenscina(Prevajalnik):

    #pri incializaciji poskrbimo za prevode besed
    def __init__(self):
        self.prevodi = {"programming":"programiranje", "pattern":"vzorec", "socket":"vtičnica"}

    #vrnemo prevedeno besedo
    def prevajanje(self, beseda):
        return self.prevodi[beseda]


class PrevajalnikNemscina(Prevajalnik):

    def __init__(self):
        self.prevodi = {"programming":"Programmierung", "pattern":"Muster", "socket":"Steckdose"}

    def prevajanje(self, beseda):
        return self.prevodi[beseda]


