
import random


stevilo_ladjic = 10
st_dovoljenih_napak = 20
vrstice = 10
stolpci = 10

# w
def polje(v, s):
    polje1 = []
    for i in range(v):
        vrstica = []
        for j in range(s):
            vrstica.append("O")
        polje1.append(vrstica)
    return polje1 

prazno_polje = polje(vrstice, stolpci)

#w
def nakljucni_indeks(v, s):
    far = []
    while len(far) < stevilo_ladjic:
        a = random.randint(0, vrstice - 1)
        b = random.randint(0, stolpci - 1)
        if [a, b] not in far:
            far.append([a, b])
    return far

# seznam_ladij = nakljucni_indeks(vrstice, stolpci)



class Igra:
    def __init__(self, seznam_ladij, poskusi=None):
        self.seznam_ladij = seznam_ladij
        self.poskusi = poskusi

    def napacni_ugibi(self):
        return [poskus for poskus in self.poskusi if poskus not in self.seznam_ladij]
        # seznam dvoenotnih seznamov

    def pravilni_ugibi(self):
        return [poskus for poskus in self.poskusi if poskus in self.seznam_ladij]
        # seznam dvoenotnih seznamov

    def stevilo_napacnih(self):
        return len(self.napacni_ugibi)
        # stevilka

    def poraz(self):
        return self.stevilo_napacnih > st_dovoljenih_napak
        # T, ce velja ^

    def potop(self):
        for i in self.seznam_ladij:
            if i not in self.poskusi:
                return False
        return True
        # T / F
    #zmaga

    def delno_pravilno(self):
        odkrito_polje = prazno_polje
        for i in self.poskusi:
            if i in self.seznam_ladij: #zadel
                odkrito_polje[i[0]][i[1]] == "X"
            else: #zgrešil
                odkrito_polje[i[0]][i[1]] == "_"
        return odkrito_polje

    def ugibaj(self, ugib):
        if len(ugib) != 2:
            return "prevelik / premajhen ugib"
        if ugib in self.poskusi:
            return "ponovljen poskus"
        else:
            self.poskusi.append(ugib)
            if ugib in self.seznam_ladij:
                if self.potop():
                    return "zmagal si"
                else:
                    return "pravilni ugib"
            else:
                if self.poraz():
                    return "izgubil si"
                else:
                    return "napačni ugib"

igra = Igra(nakljucni_indeks(vrstice, stolpci))




    



# #while vrstice not in range(5, 11):
# #    vrstice = input("Število vrstic: ")
# #
# #while stolpci not in range(5, 11):
# #    stolpci = input("Število stolpcev: ")
# 
# while stevilo_napak not in range(1, 31):
#     stevilo_napak = input("Število napak: ")


#class Ladje:
#    def __init__(self, vrs, sto):
#        self.vrs = vrs
#        self.sto = sto
#
#    def nakljucna_vrstica(self):
#        return random.randint(0, self.vrs - 1)
#
#    def nakljucni_stolpec(self):
#        return random.randint(0, self.sto - 1)
# 
##    def ladjice(self, polje1):
##        for i in range(stevilo_ladjic):
##            pass
##w
#def put_one(seznam_seznamov):
#    asd = [1] * stevilo_ladjic
#    while len(asd) > 0:
#        a = random.randint(0, 9)
#        b = random.randint(0, 9)
#        if seznam_seznamov[a][b] == 0:
#            seznam_seznamov[a][b] = asd[0]
#            asd = asd[1:]
#    return seznam_seznamov


