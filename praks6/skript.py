from moodul import *

print("Ruumi mõõdud on :")
p = float(input("Pikkus: "))
l = float(input("laius: "))
k = float(input("Kõrgus: "))

tuba = Tuba(p, l, k)

vastus = input("Kas toas on aknaid/uksi? jah/ei" )
while vastus == "jah":
    l = float(input("Akna/Ukse laius: "))
    k = float(input("Akna/Ukse kõrgus: "))
    aken_uks = AknadUksed(l, k)
    tuba.aknad_uksed.append(aken_uks)
    vastus = input("Kas toas on aknaid/uksi? jah/ei" )

print("Tapeedid on vaja kleepida " + str(tuba.tööPind()) + " ruutmeetrites")
print("Tapeedi rullide arv " + str(tuba.tapeedid(tp, tl)))
