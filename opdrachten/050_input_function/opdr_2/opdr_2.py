# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

x = True
gastenlijst = ["Jij",  ]
while x: 
    gast = str(input("Noem een gast: \n"))
    gastenlijst.append (gast)
    if gast == "x":
      x = False
    if gast == "Marie":
      gastenlijst.remove ("Marie")
    #if gast == "George":
      #gastenlijst.insert (0,"Kees")  

    if gast == "George":
            gastenlijst.remove("George")  # Eerst "George" tijdelijk verwijderen
            
            if "Kees" in gastenlijst:
                gastenlijst.insert(gastenlijst.index("Kees") + 1, "George")  # Zet George ná Kees
            else:
                gastenlijst.append("Kees")  # Voeg Kees toe als hij er nog niet is
                gastenlijst.append("George")  # Voeg George direct daarna toe
print (gastenlijst)

