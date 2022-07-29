from seznam import Seznam

#ustvarimo primer seznama
s1 = Seznam(opravila=["diplomirati", "pomiti posodo"])

#seznam s1 kloniramo
s2 = s1.prototype()

#pri izpisu obeh opazimo, da sta enaka
print(s1)
print(s2)

#seznamu s2 dodamo novo opravilo
s2.opravila.append("skuhati kavo")

#pri ponovnem izpisu opazimo, da sta seznama sedaj različna
print(s1)
print(s2)
