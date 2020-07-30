
import random


st_dovoljenih_napak = 40
vrstice = 10
stolpci = 10
slovar_ladij = {"Letalonosilka": 5, "Bojna ladja": 4, "Podmornica": 3,"Križarka": 3, "Rušilec": 2}
seznam_mest = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
ZACETEK = "B"
PRAVILNI_UGIB = "+"
PONOVLJENI_UGIB = "R"
PREMAJHEN_PREVELIK = ">"
NI_STEVILKA = "#"
NAPACNI_UGIB = "-"
ZMAGA = "W"
PORAZ = "L"


#sestavi polje 10×10
def polje(v, s):
    polje1 = []
    for i in range(v):
        vrstica = []
        for j in range(s):
            vrstica.append("O")
        polje1.append(vrstica)
    return polje1


#iz polja izbere naključne pare indeksov in jih vrne kot seznam seznamov (int med 1 in 10)
def nakljucni_indeks(v, s, slovar_l):
    seznam1 = []
    for i, j in slovar_l.items():
        seznam1.append(slovar_l[i])
    far = []
    while len(seznam1) > 0:
        for x in seznam1:
            a = random.randint(0, 1)
            if a == 0:   #vodoravno
                b = random.randint(1, v)
                c = random.randint(1, s - x + 1)
                if all([b, c + i] not in far for i in range(x)):
                    seznam1.remove(x)
                    for i in range(x):
                        far.append([b, c + i])
                else:
                    continue
            else:   #navpično
                b = random.randint(1, v - x + 1)
                c = random.randint(1, s)
                if all([b + i, c] not in far for i in range(x)):
                    seznam1.remove(x)
                    for i in range(x):
                        far.append([b + i, c])
                else:
                    continue
    return far





class Igra:
    def __init__(self, seznam_ladij, poskusi=None):
        self.seznam_ladij = seznam_ladij
        if poskusi is None:
            self.poskusi = []
        else:
            self.poskusi = poskusi

    def napacni_ugibi(self):
        return [poskus for poskus in self.poskusi if poskus not in self.seznam_ladij]
        # seznam seznamov vseh ugibov kjer ni ladjic

    def pravilni_ugibi(self):
        return [poskus for poskus in self.poskusi if poskus in self.seznam_ladij]
        # seznam seznamov vseh ugibov kjer so ladjice

    def stevilo_pravilnih(self):
        return len(self.pravilni_ugibi())
        # število najdenih ladjic

    def stevilo_napacnih(self):
        return len(self.napacni_ugibi())
        # stevilo praznih polj

    def poraz(self):
        return self.stevilo_napacnih() >= st_dovoljenih_napak

    def potop(self):
        for i in self.seznam_ladij:
            if i not in self.poskusi:
                return False
        return True
    #zmaga

    def delno_pravilno(self):
        odkrito_polje = polje(vrstice, stolpci)
        for i in self.poskusi:
            if i in self.seznam_ladij: #zadel
                odkrito_polje[i[0] - 1][i[1] - 1] = "X"
            else: #zgrešil
                odkrito_polje[i[0] - 1][i[1] - 1] = "_"
        return odkrito_polje
        # vrne polje 10×10 kjer so potopljene ladjice označene z X, zgrešena mesta z _

    def ugibaj(self, ugib):
        if len(ugib) != 2:
            return PREMAJHEN_PREVELIK
        elif ugib in self.poskusi:
            return PONOVLJENI_UGIB
        else:
            self.poskusi.append(ugib)
            if ugib in self.seznam_ladij:
                if self.potop():
                    return ZMAGA
                else:
                    return PRAVILNI_UGIB
            else:
                if self.poraz():
                    return PORAZ
                else:
                    return NAPACNI_UGIB

    def narejeno_polje(self, odkrito_polje):
        niz = ""
        for i in odkrito_polje:
             niz += " ".join(i)
             niz += " \n"
        return niz
        # vsako element v vrstici združi s presledkom in na koncu doda \n

def nova_igra():
    return Igra(nakljucni_indeks(vrstice, stolpci, slovar_ladij))


class Igre:
    def __init__(self):
        self.slovar = {}

    def novi_id(self):
        if len(self.slovar) == 0:  #če je slovar prazen
            return 0
        else:                      #naslednja številka
            return max(self.slovar.keys()) + 1

    def nova_igra(self):
        igra = nova_igra()
        id_igre = self.novi_id()
        self.slovar[id_igre] = (igra, ZACETEK) #slovar = {"id": (igra, zacetek)}
        return id_igre

    def ugibaj(self, id_igre, seznam):
        igra = self.slovar[id_igre][0]
        ugib = igra.ugibaj(seznam)
        self.slovar[id_igre] = (igra, ugib)  #slovar = {"id": (igra, ugib)}
