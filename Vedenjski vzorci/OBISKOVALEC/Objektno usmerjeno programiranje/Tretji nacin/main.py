from obiskovalec import ObiskovalecKosare
from  izdelki import *

obiskovalec=ObiskovalecKosare()

print(obiskovalec.obisci(Sadje(12, 3)))
print(obiskovalec.obisci(Sadje(12, 3), 15))
print(obiskovalec.obisci(Knjiga(12)))

