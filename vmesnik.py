import model

def izpis_igre(igra):
    tekst = (
        "{polje}\n"
        "=================================================\n"
        "Število preostalih preizkusov: {stevilo_preostalih_poskusov} \n"
        "Poskusi: {ugibani}\n"
        "================================================="
    ).format(
        polje=igra.narejeno_polje(igra.delno_pravilno()),
        stevilo_preostalih_poskusov=model.st_dovoljenih_napak - igra.stevilo_napacnih(),
        ugibani=igra.poskusi
    )
    return tekst


def izpis_zmage(igra):
    tekst = (
        "\nZmagal si!\n\n"
    )
    return tekst  


def izpis_poraza(igra):
    tekst = (
        "\nIzgubil si :(. Ladjice so se skrivale na: {mesta}\n\n"
    ).format(
        mesta=igra.seznam_ladij
    )
    return tekst 

def izpis_napake():
    tekst = (
        "::::::::Vnesi številko vrstice, številko stolpca (med 1 in {stevilo})!::::::::\n"
    ).format(
        stevilo=model.vrstice
    )
    return tekst


def vnos_vrstice_in_stolpca():
    return input("Vrstica, stolpec(loči z vejico): ").split(',')


def pozeni_vmesnik():

    igra = model.nova_igra()

    while True:
        print(izpis_igre(igra))
        poskus = vnos_vrstice_in_stolpca()
        poskus_seznam = [int(x) for x in poskus if x in model.seznam_mest]
        asdf = igra.ugibaj(poskus_seznam)
        if asdf == model.PREMAJHEN_PREVELIK:
            print(izpis_napake())
        elif asdf == model.ZMAGA:
            print(izpis_zmage(igra))
            ponovni_zagon = input("Za ponovni zagon vpišite R. ").strip()
            if ponovni_zagon.strip().lower() == "r":
                igra = model.nova_igra()
            else:
                break
        elif asdf == model.PORAZ:
            print(izpis_poraza(igra))
            ponovni_zagon = input("Za ponovni zagon vpišite R. ").strip()
            if ponovni_zagon.strip().lower() == "r":
                igra = model.nova_igra()
            else:
                break


pozeni_vmesnik()
