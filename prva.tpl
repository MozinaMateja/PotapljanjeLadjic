%rebase("base.tpl", title="prva")
    <h1>Potapljanje ladjic</h1>
    <h2>Opis igre</h2>
    <p>Na plošči velikosti 10×10 se skriva 5 ladjic različnih velikosti:</p>
    <ul>
        <li> letalonosilka dolžine 5,</li>
        <li> bojna ladja dolžine 4,</li>
        <li> podmornica dolžine 3,</li>
        <li> križarka dolžine 3 in</li>
        <li> rušilec dolžine 2.</li>
    </ul>
    <p>Ladjice so postavljene vodoravno ali navpično (ne diagonalno) in se med seboj lahko dotikajo.</p>
    <p>Kje je ladjica ugibate tako, da vpišete številko stolpca in številko vrstice. 
        Če ste zadeli, se bo na tem mestu pojavil "X", če ste zgrešili pa "_".</p>
    <p>Na voljo imate 40 poskusov.</p>
    <form action="/nova_igra/" method=post>
        <button type="submit">Nova igra</button>
    </form>
