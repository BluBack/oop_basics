from praks4.sõdur import Sodur
from random import randint


armee_1 = []
armee_2 =[]

for kord in range(20):
    millisesse_armeese = randint(1, 2)
    sodur = Sodur(millisesse_armeese)

    if(  millisesse_armeese == 1):
        armee_1.append(sodur)

    if (millisesse_armeese == 2):
        armee_2.append(sodur)


print("Armee 1")
for SOdur in armee_1:
    sodur.info()

print("-----------------------------")

print("Armee 2")
for sõdur in armee_2:
    sodur.info()