#Név;    Neme;    Részleg;    Belépés;    Bér

# 0         1       2            3          4

with open("berek2020.txt","r",encoding="UTF-8") as f:
    fejlec = f.readline()
    lista = [sor.strip().split(";") for sor in f]
    
print(f"3.feladat: Dolgozók száma: {len(lista)} fő")

berek = [int(sor[4]) for sor in lista]

print(f"4.feladat: Bérek átlaga: {(sum(berek) / len(lista)) / 1000:.1f} eFt")

bekeres = input("5.feladat: Kérem egy részleg nevét: ")

megadatott_reszleg = [(sor[4],sor) for sor in lista if sor[2] == bekeres]

if megadatott_reszleg:
    nagy,adat = max(megadatott_reszleg)
    print(f"""6.feladat: A legtöbbet kereső dolgozó a megadott részlegen
        Név: {adat[0]}
        Neme: {adat[1]}
        Belépés: {adat[3]}
        Bér: {nagy} Forint""")
else:
    print("6.feladat: A megadott részleg nem létezik a cégnél!")

print("7.feladat: Statisztika")

stat = dict()
for sor in lista:
    stat[sor[2]] = stat.get(sor[2],0) + 1
    
statisztika = [print(f"        {reszleg} - {db} fő") for reszleg,db in stat.items()]

