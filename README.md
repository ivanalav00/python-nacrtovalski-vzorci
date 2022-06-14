# UPORABA GANG OF FOUR NAČRTOVALSKIH VZORCEV V PROGRAMSKEM JEZIKU PYTHON

Tehnološki standardi so pomemben del informacijskega sveta. Uporaba priznanih in dolgoletno postavljenih metod, tehnologij ter postopkov vodi v kvaliteto in zanesljivost tistega, kar razvijamo. Zaradi enakih razlogov pa bi lahko rekli, da je bistvenega pomena razvijanje rešitev, ki jih lahko ponovno uporabimo in uporaba kode, komponent in rešitev, za katere vemo, da so stabilne. Izkušeni programski inženirji vedo, da večjo težo nosi znanje, kako pravilno izkoristiti razpoložljive vire, kot pa odkrivanje že odkritega.

Poleg komponent in konkretne kode lahko pri razvoju programske opreme ponovno uporabimo tudi ideje. Načrtovalski vzorci so prav to, abstraktne ideje za probleme, s katerimi se pogosto srečujemo. Ne predstavljajo konkretne rešitve, zato jih lahko uporabimo na različne načine ter jih prilagodimo za svoj specifičen problem.

## Kaj so načrtovalski vzorci? 

Na višji ravni arhitekture programske opreme imamo arhitekturne vzorce, ki definirajo strukturo in obliko programske opreme. Nižje po ravneh ko gremo, prej se srečamo z abstraktnejšimi idejami, kot so namen programske opreme in obnašanje ter komunikacija modulov. Načrtovalski vzorci so nižjenivojski načrt programske opreme, ki se ukvarja s ponovno uporabo rešitev problemov, s katerimi se kot razvijalci pogosto srečujemo. Rešujejo jedro nekega problema, samo rešitev pa lahko nato uporabimo na nešteto različnih načinov. Združujejo znanje kolektivnih izkušenj inženirjev programske opreme, s tem, da se zaradi njihove abstraktnosti lahko uspešno aplicirajo tudi v primerih, kjer problem ni najbolj poznan.

Z načrtovalskimi vzorci GoF se srečujemo predvsem, kadar govorimo o objektno orientiranih jezikih, igrajo pa tudi veliko vlogo pri objektno usmerjenem razvojnem procesu. Zmanjšujejo kompleksnost na način, da definirajo abstrakcije, ustvarjajo slovar za načrtovanje in kot že prej omenjeno, združujejo izkušnje reševanja pogostih problemov. Uporaba načrtovalskih vzorcev pri takšnih procesih zagotavlja prednost predvsem pri ponovni uporabi, kjer lahko razvijalec takoj prepozna problem in nato izkoristi bogat ekosistem vzorcev, brez da bi pri tem ponovno odkrival že znane dokazano uspešne pristope zaznanega problema.

Vzorce GoF lahko kategoriziramo glede na namena v naslednje skupine: ustvarjalne, strukturne in vedenjske vzorce. Ti tri kategorije vzorcev pa prav tako predstavljajo življenjski cikel reševanja problemov in časa izvajanja programske kode.

## Programski jezik Python in načrtovalski vzorci

Python je programski jezik, ki je uporabljen na mnogovrstne načine na raznolikih domenah. Zaradi svoje dinamičnosti in preprostosti ga lahko izkoristimo kjerkoli potrebujemo hiter razvoj programske opreme. Njegovo aplikacijo najdemo na področjih sistemskih pripomočkov, spletnih strani, grafičnih vmesnikov, porazdeljenega programiranja, procesiranja slik, dostopa do podatkovnih baz in še mnogih drugih domenah. 

Zakaj bi ga pa izkoristili na področju programske arhitekture in še bolj specifično, zakaj na področju načrtovalskih vzorcev? Python ima nekaj značilnosti, ki jih je smiselno upoštevati pri razvoju s pomočjo načrtovalskih vzorcev:
- **Kvaliteta**: Python kot jezik omogoča pisanje kode, ki jo je enostavno ponovno uporabiti in vzdrževati, kar je pomembno tudi v kontekstu načrtovalskih vzorcev. Znan je po berljivosti, kar vodi v univerzalno razumevanje različnih izkušenj programskih inženirjev.
- **Objektno-orientiran jezik**: Python je 100% objektno-orientiran jezik, kar pomeni, da je vsaka stvar v jeziku Python objekt, kar je pomembno, saj se z načrtovalskimi vzorci GoF  srečujemo predvsem pri objektno-orientiranih jezikih. 
- **Dinamičnost in interaktivnost**: s svojo dinamičnostjo Python omogoča fleksibilnost in posledično omogoča več načinov implementacije enega vzorca.

Poleg prednosti, ki jih Python lahko doprinese, pa se je potrebno zavedati, da bi prednosti uporabe vzorcev lahko izkoristili pri kateremkoli jeziku. Z implementacijo vzorcev naši kodi dodamo red in s tem prispevamo potrebne omejitve za doseg jasnosti – kaj lahko naredimo in kaj ne. Tako da vprašanje ni, zakaj bi uporabili Python za načrtovalske vzorce, ampak katere vzorce je smiselno uporabiti glede na njegovo naravo.

### Implementacija vzorcev 

Na repozitoriju je prikazana implementacija različnih vzorcev na mnogovrstne načine. Osredotočili smo se na objektno usmerjeno programiranje, metaprogramiranje, na prikaz vzorcev s pomočjo Python knjižnice PyPattyrn in prikaz, na kakšen način so nekateri vzorci že vgrajeni v Pyton. Poleg vzorcev sta predstavljena tudi uporaba anti-vzorcev in združevanje načrtovalskih vzorcev.

## Viri
R. C. Martin, “Design Principles and Design Patterns,” 2000, Accessed: Jun. 06, 2022. [Online]. Available: www.objectmentor.com

A. Balachandran Pillai, Software Architecture with Python. Packt Publishing, Ltd., 2017.

E. Gamma, R. Helm, R. Johnson, and J. Vlissides, “Design Patterns: Abstraction and Reuse of Object-Oriented Design,” Lecture Notes in Computer Science (including subseries Lecture Notes in Artificial Intelligence and Lecture Notes in Bioinformatics), vol. 707 LNCS, pp. 406–431, 1993, doi: 10.1007/3-540-47910-4_21.

A. Boyanov, “Python Design Patterns Guide | Toptal,” Developers. https://www.toptal.com/python/python-design-patterns (accessed Mar. 31, 2022).

M. Lutz, Programming Python, Druga izdaja. 101 Morris Street, Sebastopol, CA: O’Reilly & Associates, Inc., 2001.




