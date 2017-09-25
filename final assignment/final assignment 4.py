def standaardtarief(afstandKM):
    if int(afstandKM)< 50:
        uitkomst = afstandKM * 0.80
        return uitkomst
    if int(afstandKM) <= 0:
        uitkomst = 0
        return uitkomst
    else:
        uitkomst = (afstandKM*0.60) + 15
        return uitkomst


def ritprijs(leeftijd, weekendrit, afstandKM):
    standaardtarief(afstandKM)
    if weekendrit == "ja" and (leeftijd < 12 or leeftijd >= 65):
        reisprijs = standaardtarief(afstandKM) * 0.65
        return(reisprijs)
    elif weekendrit == "nee" and (leeftijd < 12 or leeftijd >= 65):
        reisprijs = standaardtarief(afstandKM) * 0.70
        return (reisprijs)
    elif weekendrit == "ja" and leeftijd >= 12  and leeftijd < 65:
        reisprijs = standaardtarief(afstandKM) * 0.60
        return(reisprijs)
    else:
        return(standaardtarief(afstandKM))


afstandKM = int (input("hoeveel Km heb je gereden"))
weekendrit = input("is het weekend")
leeftijdsgroep =int (input("wat is uw leeftijd"))
print (ritprijs(leeftijdsgroep, weekendrit, afstandKM))


