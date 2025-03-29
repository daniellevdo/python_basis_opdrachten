# Opdracht 4 Tekst opslaan
# Naam student:
# Groep:


# Party enquete

vraag1 = ("Wat is je voornaam?\n")
vraag2 = ("Wat is je achternaam?\n")
vraag3 = ("Wat neem je aan drank mee?\n")
vraag4 = ("Wat neem je mee om te eten?\n")

antwoordenlijst = []

antwoord1 = input(vraag1)
antwoord2 = input(vraag2)
antwoord3 = input(vraag3)
antwoord4 = input(vraag4)
antwoordenlijst.append (antwoord1)    
antwoordenlijst.append (antwoord2)    
antwoordenlijst.append (antwoord3)    
antwoordenlijst.append (antwoord4)    

with open('party-info.txt', 'wt') as fo:
    for antwoord in antwoordenlijst:
        fo.write(antwoord + "\n")
    