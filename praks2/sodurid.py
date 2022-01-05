from random import randint

from praks2.sodur import Sodur

sodur1 = Sodur()
sodur2 = Sodur()

while(sodur1.tervis > 0 and sodur2.tervis > 0):
    kes_loob = randint(1, 2)
    if(kes_loob == 1):
        print("Esimene lööb teist")
        sodur2_tervis = sodur2.tervis - 20
        print("Teise sõduri tervis = " + str(sodur1.tervis))
    if(kes_loob == 2):
        print("Teine lööb esimest")
        sodur1.tervis = sodur1.tervis - 20
        print("Esimese sõduri tervis = " + str(sodur1.tervis))

    if(sodur1.tervis == 0):
        print("Teine sõdur on võitnud")
    else:
        print("Esimene sõdur on võitnud")
