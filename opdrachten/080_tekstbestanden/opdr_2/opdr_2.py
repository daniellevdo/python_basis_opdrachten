# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

import random
prompt = "Raad mijn geheime getal \n"
geheim_getal = random.randint(1, 100)
pogingen = 0

active = True
while active:
  message = int(input(prompt))
  pogingen += 1
  if message < geheim_getal:
      print("hoger")
  if message > geheim_getal:
      print ("lager")
  if message == geheim_getal:
      print (f"Je hebt het getal in {pogingen} pogingen geraden, het is {geheim_getal} !")
      break
