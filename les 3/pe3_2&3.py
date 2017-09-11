leeftijd = eval(input('wat is je leeftijd..'))
paspoort = input('heb je een nederlands paspoort..')
if leeftijd > 17 and paspoort == 'ja':
    print('je mag stemmen')
else:
    print('helaas mag je niet stemmen')
