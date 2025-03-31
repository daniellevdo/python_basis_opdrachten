# Opdracht 1 functies
# Naam student:
# Groep:


def write_to_file(afile, atext):
    fo = open(afile, 'wt')
    fo.write(atext)
    fo.close()

my_tekst = "Schrijf dit maar even in een bestandje"
my_file = "test.txt"

write_to_file(my_file, my_tekst)
