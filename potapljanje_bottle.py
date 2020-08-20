import bottle 
import model

SKRIVNOST = "skrivnost"
potapljanje = model.Igre()


@bottle.get('/')  #prva stran
def prva():
    return bottle.template('prva.tpl')

@bottle.post('/nova_igra/')
def nova_igra():
    id_igre = potapljanje.nova_igra()
    bottle.response.set_cookie("idigre", id_igre, secret=SKRIVNOST, path='/')
    bottle.redirect('/igra/')


@bottle.get('/igra/')
def naredi():
    id_igre = bottle.request.get_cookie('idigre', secret=SKRIVNOST)
    igra, ugib = potapljanje.slovar[id_igre]
    return bottle.template('igra.tpl', igra=igra, ugib=ugib)

@bottle.post('/igra/')
def ugibaj():
    id_igre = bottle.request.get_cookie('idigre', secret=SKRIVNOST)
    mesto = [int(bottle.request.forms['vrstica']), int(bottle.request.forms['stolpec'])]
    potapljanje.ugibaj(id_igre, mesto)
    bottle.redirect('/igra/')

bottle.run(debug=True, reloader=True)

