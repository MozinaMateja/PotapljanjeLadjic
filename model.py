
import random


stevilo_ladjic = 10
st_dovoljenih_napak = 20
vrstice = 10
stolpci = 10
seznam_mest = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
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

prazno_polje = polje(vrstice, stolpci)


#iz polja izbere naključne pare indeksov in jih vrne kot seznam seznamov
def nakljucni_indeks(v, s):
    far = []
    while len(far) < stevilo_ladjic:
        a = random.randint(1, vrstice)
        b = random.randint(1, stolpci)
        if [a, b] not in far:
            far.append([a, b])
    return far

# seznam_ladij = nakljucni_indeks(vrstice, stolpci)



class Igra:
    def __init__(self, seznam_ladij, poskusi=[]):
        self.seznam_ladij = seznam_ladij
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
        odkrito_polje = prazno_polje
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
    return Igra(nakljucni_indeks(vrstice, stolpci))



