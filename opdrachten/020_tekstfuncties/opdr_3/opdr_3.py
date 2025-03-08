# Opdracht 3 tekstfuncties
# Naam student:
# Groep:

# Hier komt je code...


a = "    *"
b = "   ***"
c = "  ******"
d = " ********"
e = "***********"
f = "    ***"
g = "    ***"
h ="    ***"

boom = (f"{a}\n{b}\n{c}\n{d}\n{e}\n{f}\n{g}\n{h}")   
for line in boom:
    print("   ".join([line] * 5))

tree = [
    "   *   ",
    "  ***  ",
    " ***** ",
    "*******",
    "  ***  "
]

for line in tree:
    print("   ".join([line] * 5))