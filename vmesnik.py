
import model

def izpis_igre(igra):
    tekst = (
        "{polje}\n"
        "=================================================\n"
        "Število preostalih preizkusov: {stevilo_preostalih_poskusov} \n"
        "Poskusi: {ugibani}\n"
        "Število potopljenih ladjic: {stevilo_potopljenih} od {stevilo_iskanih}\n"
        "================================================="
    ).format(
        polje=igra.narejeno_polje(igra.delno_pravilno()),
        stevilo_preostalih_poskusov=model.st_dovoljenih_napak - igra.stevilo_napacnih(),
        ugibani=igra.poskusi,
        stevilo_potopljenih=igra.stevilo_pravilnih(),
        stevilo_iskanih=model.stevilo_ladjic
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


def vnos_vrstice_in_stolpca():
    return input("Vrstica, stolpec(loči z vejico): ").split(',')


def pozeni_vmesnik():

    igra = model.nova_igra()

    while True:
        print(izpis_igre(igra))
        poskus = vnos_vrstice_in_stolpca()
        poskus_seznam = [int(x) for x in poskus]
        igra.ugibaj(poskus_seznam)
        if igra.potop():
            print(izpis_zmage(igra))
            break
        elif igra.poraz():
            print(izpis_poraza(igra))
            break


pozeni_vmesnik()
