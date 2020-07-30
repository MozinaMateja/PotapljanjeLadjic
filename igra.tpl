%import model
<!DOCTYPE html>
<html lang="sl">
<head>
    <meta charset="utf-8"/>
    <title>Potapljanje ladjic</title>
</head>

<body>
    <table>
        %for i in range(len(igra.delno_pravilno())):
        <tr>
            %for j in range(len(igra.delno_pravilno()[0])):
            <td>{{igra.delno_pravilno()[i][j]}}</td>
            %end
        </tr>
        %end
    </table>
<h2>Število poskusov: {{model.st_dovoljenih_napak - igra.stevilo_napacnih()}}</h2>
%if ugib == model.ZMAGA:
<h1>ČESTITKE, ZMAGAL SI!</h1>
<form action="/igra/" method="post">
    <button type="submit">Nova igra</button>
</form>

%elif ugib == model.PORAZ: 
<h2>Ladjice so se skrivale na: {{igra.seznam_ladij}}</h2>
<h1>IZGUBIL SI. POSKUSI PONOVNO?</h1>
<form action="/igra/" method="post">
    <button type="submit">Nova igra</button>
</form>

%else:
<form action="/igra/{{id_igre}}/" method="post">
    Vrstica: <input type="number" name ="vrstica" min="1" max="10" required>
    Stolpec: <input type="number" name ="stolpec" min="1" max="10" required>
    <button type="submit">Streljaj</button>
</form>
%end
</body>
</html>