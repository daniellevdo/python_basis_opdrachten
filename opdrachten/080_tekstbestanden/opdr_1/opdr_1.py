# Opdracht 1 while-loops
# Naam student:
# Groep:


prompt = ("Wat vind je van de huidige regering?\n\
Wat vind je van de Python-lessen tot nu toe?\n\
Wat vind jij de mooiste stad van Nederland?\n")

active = True
lst = []
while active:
    message = input(prompt)
    if message == 'q':
        active = False
        fo = open('enquete.txt', 'wt')
        for i in lst:
            fo.write(i + "\n")
        fo.close()
    else:
        lst.append (message)    