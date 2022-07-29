from tovarna import TovarnaPrevajalnikov

#vprašamo po vnosu željenega jezika in besede
jezik = input("Jezik prevoda: ")
beseda = input("Beseda v anglescini: ")

#ustvarimo prevajalnik glede na vnos
prevajalnik = TovarnaPrevajalnikov.ustvari(jezik)

#izpišemo prevedeno besedo
print(prevajalnik.prevajanje(beseda))
