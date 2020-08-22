import bottle 
import model

SKRIVNOST = "skrivnost"
DATOTEKA_S_STANJEM = "stanje.json"

potapljanje = model.Igre(DATOTEKA_S_STANJEM)
potapljanje.nalozi()


@bottle.get('/')  #prva stran
def prva():
    return bottle.template('prva.tpl')


@bottle.post('/nova_igra/')
def nova_igra():
    id_igre = potapljanje.nova_igra()
    bottle.response.set_cookie("idigre", "idigre{}".format(id_igre), secret=SKRIVNOST, path='/')
    bottle.redirect('/igra/')


@bottle.get('/igra/')
def naredi():
    id_igre = int(bottle.request.get_cookie('idigre', secret=SKRIVNOST).split("e")[1])
    igra, ugib = potapljanje.slovar[id_igre]
    return bottle.template('igra.tpl', igra=igra, ugib=ugib)


@bottle.post('/igra/')
def ugibaj():
    id_igre = int(bottle.request.get_cookie('idigre', secret=SKRIVNOST).split("e")[1])
    mesto = [int(bottle.request.forms['vrstica']), int(bottle.request.forms['stolpec'])]
    potapljanje.ugibaj(id_igre, mesto)
    bottle.redirect('/igra/')

bottle.run(debug=True, reloader=True)

