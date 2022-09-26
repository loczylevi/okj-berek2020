class Berek:
    def __init__(self,sor):
        nev,nem,reszleg,belepes,ber = sor.strip().split(";")
        self.nev = nev
        self.nem = nem
        self.reszleg = reszleg
        self.belepes = belepes
        self.ber = int(ber)
        
with open("berek2020.txt","r",encoding="UTF-8") as f:
    fejlec = f.readline()
    lista = [Berek(sor) for sor in f]
    
print(f"3.feladat: Dolgozók száma: {len(lista)} fő")

berek = [sor.ber for sor in lista]

print(f"4.feladat: Bérek átlaga: {(sum(berek) / len(lista)) / 1000:.1f} eFt")

bekeres = input("5.feladat: Kérem egy részleg nevét: ")

megadatott_reszleg = [(sor.ber,sor) for sor in lista if sor.reszleg == bekeres]

megadatott_reszleg = [(sor.ber,sor) for sor in lista if sor.reszleg == bekeres]

if megadatott_reszleg:
    nagy,adat = max(megadatott_reszleg)
    print(f"""6.feladat: A legtöbbet kereső dolgozó a megadott részlegen
        Név: {adat.nev}
        Neme: {adat.nem}
        Belépés: {adat.belepes}
        Bér: {nagy} Forint""")
else:
    print("6.feladat: A megadott részleg nem létezik a cégnél!")

print("7.feladat: Statisztika")

stat = dict()
for sor in lista:
    stat[sor.reszleg] = stat.get(sor.reszleg,0) + 1
    
statisztika = [print(f"        {reszleg} - {db} fő") for reszleg,db in stat.items()]