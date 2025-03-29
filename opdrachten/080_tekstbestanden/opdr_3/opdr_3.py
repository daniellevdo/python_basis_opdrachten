# Opdracht 3 Tekst opslaan
# Naam student:
# Groep:


vraag = "Geef me een geheim\n" \
        "vul een 'q' in om te stoppen\n" 

while True:
  geheim = input(vraag)

  if geheim == 'q':
    break

  geheimtaal = ""

  for char in geheim:
      if char.isalpha():
        shift = 5
      
        if char.islower():
          new_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
        elif char.isupper():
                new_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        geheimtaal += new_char
      else:
        geheimtaal = char

  print("Versleuteld geheim:", geheimtaal)
 






