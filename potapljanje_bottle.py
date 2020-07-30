import bottle 
import model

potapljanje = model.Igre()


@bottle.get('/')  #prva stran
def prva():
    return bottle.template('prva.tpl')


@bottle.post('/igra/')
def nova_igra():
    id_igre = potapljanje.nova_igra()
    bottle.redirect('/igra/{}/'.format(id_igre))


@bottle.get('/igra/<id_igre:int>/')
def naredi(id_igre):
    igra, ugib = potapljanje.slovar[id_igre]
    return bottle.template('igra.tpl', id_igre=id_igre, igra=igra, ugib=ugib)

@bottle.post('/igra/<id_igre:int>/')
def ugibaj(id_igre):
    mesto = [int(bottle.request.forms['vrstica']), int(bottle.request.forms['stolpec'])]
    potapljanje.ugibaj(id_igre, mesto)
    bottle.redirect('/igra/{}/'.format(id_igre))

bottle.run(debug=True, reloader=True)

