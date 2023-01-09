import random

subor = open("skok_do_dialky.txt", "r")

krajiny = []
cigan = []
aasa = []
skok = []
meno = []
najvaac = []
miropele = 0
dsd = 0
nja = 0
nigg = 0
for riadok in subor:
    riadok = riadok.strip()
    riadok = riadok.split()
    krajiny.append(riadok[1])
    meno.append(riadok[0])
    skok.append(riadok[2:])
    miropele = miropele + 1


aasa = [*set(krajiny)]

for krajina in aasa:
    cigan.append(krajiny.count(krajina))


print("krajiny:", aasa)

print("pocet sutaziacich:", miropele)
for i in skok:
    dsd = dsd + 1
    for j in range(5):
        if int(i[j]) > nja:
            nja = int(i[j])
            nigg = dsd-1

najvaac.append(meno[nigg])
for i in skok:
    
    for j in range(5):
        if (int(i[j]) == nja) and (meno[dsd-1] not in najvaac):
            najvaac.append(meno[dsd-1])
            
print("najdalej skocil:", najvaac)
