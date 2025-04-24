# Opdracht 1 functies
# Naam student:
# Groep:

# importeer de module csv...
import sys
import os

# Voeg de map 'my_modules' toe aan het Python importpad
sys.path.append(os.path.join(os.path.dirname(__file__), "my_modules"))

# Importeer je eigen csv-module (my_csv.py)
import my_csv

# Pad naar het CSV-bestand
csv_path = os.path.join(os.path.dirname(__file__), "test.csv")

# Verwerk de CSV-data
persons = []
with open(csv_path, 'rt') as file:
    for line in file:
        lst = my_csv.sanitize(line)
        person = my_csv.create_person(lst)
        person = my_csv.add_fullname(person)
        persons.append(person)

# Toon alle personen
print("Alle personen:")
my_csv.print_persons(persons)

# Test filters
print(my_csv.do_filter("achternaam", "V", persons))

print(my_csv.do_filter("plaats", "d", persons))


