# Opdracht 3 condities
# Naam student:
# Groep:

normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd_range = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}
prijs_na_korting1 = normale_toegangsprijs * (1 - kortings_percentages ["kinderen"] / 100)
prijs_na_korting2 = normale_toegangsprijs * (1 - kortings_percentages ["volwassenen"] / 100)
prijs_na_korting3 = normale_toegangsprijs * (1 - kortings_percentages ["ouderen"] / 100)

leeftijd = int(input("Geef uw leeftijd in aantal jaar \n"))

for leeftijd in leeftijd_range:
  if leeftijd == "baby":
    print ("U behoort tot de groep baby","\nU krijgt ", kortings_percentages ["baby"], "% korting\nU betaald niks")

  if leeftijd == "kinderen":
    print ("U behoort tot de groep kinderen \nU krijgt ", kortings_percentages ["kinderen"], "% korting\n")
    print ("U betaald daarom", prijs_na_korting1)    
  if leeftijd == "volwassenen":
    print ("U behoort tot de groep Volwassenen \nU krijgt ", kortings_percentages ["volwassenen"], "% korting\n")
    print ("U betaald daarom", prijs_na_korting2)     
  if leeftijd == "ouderen":
    print ("U behoort tot de groep ouderen \nU krijgt ", kortings_percentages ["ouderen"], "% korting\n")
    print ("U betaald daarom", prijs_na_korting3) 

    