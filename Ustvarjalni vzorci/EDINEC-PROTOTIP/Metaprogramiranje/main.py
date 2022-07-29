from seznam import Seznam

#ustvarimo primer seznama
s1 = Seznam(opravila=["diplomirati", "pomiti posodo"])
s2 = Seznam(opravila=["skuhati kavo"])

print(s2 is s1) #True - delita si instance

# seznam opravil je enak, čeprav smo seznamu s2 določili druga opravila
print(s2)

#seznam s1 kloniramo
s3 = s1.kloniraj()

print(s3 is s1) #False - ne delita si instance

#pri izpisu obeh opazimo, da sta enaka
print(s1)
print(s3)

#seznamu s3 dodamo novo opravilo
s3.opravila.append("skuhati kavo")

#pri ponovnem izpisu opazimo, da sta seznama sedaj različna
print(s1)
print(s3)

