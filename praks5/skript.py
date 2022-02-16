#impoerdime vajalikud klassid
from moodul import *
#küsime kasutajalt andmeid
print("Ruumi mõõdud on :")
p = float(input("Pikkus: "))
l = float(input("laius: "))
k = float(input("Kõrgus: "))
#loome toa objekti
tuba = Tuba(p, l, k)
#lisame vajadusel aknad ja uksed
vastus = input("Kas toas on aknaid/uksi? jah/ei" )
while vastus == "jah":
    #küsime nende mõõdud
    l = float(input("Akna/Ukse laius: "))
    k = float(input("Akna/Ukse kõrgus: "))
    #loome akna ja ukse objektid
    aken_uks = AknadUksed(l, k)
    #lisame akna või ukse toa sisse
    tuba.aknad_uksed.append(aken_uks)
    vastus = input("Kas toas on aknaid/uksi? jah/ei" )
#küsime tapeedi rulli mõõdud
tl = float(input("Tapeedi rulli laius: "))
tp = float(input("Tapeedi rulli pikkus: "))
#väljastame arvutatud tulemused
print("Tapeedid on vaja kleepida " + str(tuba.tööPind()) + " ruutmeetrites")
print("Tapeedi rullide arv " + str(tuba.tapeedid(tp, tl)))

