class Auto:
    def __init__(self, merk):
        self.merk = merk
    def versnellen(self, snelheid):
        print(f"Ik ben een {self.merk} en versnel met {snelheid} km per uur")
def stopen(self):
        print(f"Ik ben een {self.merk} en stop nu")

auto = Auto(merk="BMW", model="X5")  # instantie van 1 auto maken
auto2 = Auto(merk="vw", model="Golf")  # instantie van 2 auto maken

auto.versnellen(10)
print(auto.merk)

auto2.versnellen(20)

print(auto.snelheid) 

auto.stopen() # foutmelding, want snelheid is geen attribuut van auto, maar een parameter van de methode versnellen

auto.merk = "mersedesbenz"