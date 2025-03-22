# Opdracht 4 condities
# Naam student:
# Groep:



toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00) , ("ansjovis", 2.50)]
beschikbare_toppings = [naam for naam, prijs in toppings]

keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings} \n")
for naam, prijs in toppings:
  if keuze == naam:
    print ("U hebt ", keuze, "besteld. Dat kost ", prijs)
    break
else:
  print ("Uw keuze zit niet in ons assortiment")  
  
  