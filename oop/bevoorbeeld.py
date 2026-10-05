class Dier:
    def __init__(self, naam):
        self.naam = naam

    def geluid(self):
        return "..."  # Placeholder for the actual sound a animal makes

class Hond(Dier):
    def geluid(self):
        return "woef"

# Create an instance of the Hond class
h = Hond("Rex")
print(h.naam, h.geluid())

class kat(Dier):
    def geluid(self):
        return "miauw"
# Create an instance of the kat class
k = kat("Whiskers")
print(k.naam, k.geluid())

class Varken(Dier):
    def geluid(self):
        return "knor"
v = Varken("Babe")
print(v.naam, v.geluid())

class hound(Dier):
    def geluid(self):
        return "blaff"
h = hound("Buddy")
print(h.naam, h.geluid())
