from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom', handlesnull=True)
def blobjpg_to_html(blob,style,feature,parent):
    """
    Restituisce il blob (che deve essere un jpeg) convertito in HTML img data url per visualizzarlo
    <br> in un Widget HTML o in un suggerimento mappa.
    <br>E' obbligatorio il secondo parametro style. 
    <br>Il parametro style puo' assumere il valore '' per nessuno stile (dimensioni originali) 
    <br>o può essere una stringa CSS di stile per img HTML tag,
    <br>Se stile = 'Null' viene applicato di default 'style="max-width:100%; max-height:100%;'.
    <p style="color:Olive"><b>Sintassi</b></p>
    <p style="color:blue"><b>blobjpg_to_html</b><mark style="color:black">(</mark>
    <mark style="color:red">blob</mark><mark style="color:black">,</mark><mark style="color:red">style</mark><mark style="color:black">)</mark>
    <p style="color:Olive"><b>Argomenti</b></p>
    <p style="color:red"><b>blob  </b><mark style="color:black"> - campo contenente i dati blob</mark><br>
    <mark style="color:red"><b>style </b><mark style="color:black"> - campo contenente stringa CSS</mark>
    <p style="color:Olive"><b>Esempi</b></p>
        <ul>
            <li><mark><i> blobjpg_to_html("photo", '') -> tag img con immagine a risoluzione originale</mark></li>
            <li><mark><i> blobjpg_to_html("photo", Null) -> tag img con dimensioni massime </mark></li>
            <li><mark><i> blobjpg_to_html("photo", 'width="250" height="250"')   -> tag img dimensionato</mark></li>
        </ul>
    
    Tratto da https://gis.stackexchange.com/questions/350541/display-photo-stored-as-blob-in-gpkg
    """
    blob64 = blob.toBase64().data().decode()
    if style is None:
        stylestring = 'style="max-width:100%; max-height:100%;"'
    elif not(style):
        stylestring = 'style=""'
    else:
        stylestring = 'style="' + style + '"'
    fullstring = '<img src="data:image/jpeg;base64,' + blob64 + '" ' + stylestring + ' alt="Invalid jpeg">'
    return fullstring