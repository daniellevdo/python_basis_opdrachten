# Opdracht 1 input function
# Naam student:
# Groep:

# Hier komt je code, maak gebruik van de input functie om de lengte van de rechthoekzijden van de driehoek op te vragen.

#> Geef de lengte van de eerste zijde  
#> 4  
#> Geef de lengte van de tweede zijde  
#> 3  
#> 
#> De lengte van de schuine zijde is: 5

import math


zijde1 = int(input("Geef de lengte van de eerste zijde \n"))
zijde2 = int(input("Geef de lengte van de tweede zijde \n"))

zijde3 = int((zijde1*zijde1 + zijde2*zijde2))
zijde4 = math.sqrt(zijde3)
print ("De lengte van de schuine zijde is: ")
print (zijde4)

