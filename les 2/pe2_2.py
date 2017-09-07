CijferICOR = 6
cijferPROG = 7
cijferCSN = 5

cijferlijst = CijferICOR + cijferCSN + cijferPROG

gemiddelde = cijferlijst / 3
beloning = cijferlijst * 30

overzicht = ' mijn cijfers (gemiddeld een' , int(gemiddelde),' leveren beloning op van', int(beloning)

print(overzicht)