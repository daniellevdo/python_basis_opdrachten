# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

stedenlijst = []
#while True:
 #   stad = input("Geef een naam van een stad:\n")
  #  if stad == "x":
   #   break

    #stedenlijst.append (stad)
#print (stedenlijst)

while True:
    stad = input("Geef een naam van een stad:\n").strip()
    
    if stad.lower() == "x":  # Voorkomt dat 'X' of ' x ' problemen veroorzaakt
        break

    stedenlijst.append(stad)

# Sorteer de lijst van Z naar A
stedenlijst_sorted = sorted(stedenlijst, reverse=True)

print(stedenlijst_sorted)


