class Persoon:
    def __init__(self, naam, leeftijd):
        self.naam = naam
        self.leeftijd = leeftijd

    def __str__(self):
        return f"{self.naam} is {self.leeftijd} jaar oud."

class Docent(Persoon):
    def __init__(self, naam, leeftijd, vak):
        super().__init__(naam, leeftijd)
        self.vak = vak

    def __str__(self):
        return f"{super().__str__()} Hij/zij geeft het vak {self.vak}."

docenten_lijst = [
    Docent("William", 45, "Python"),
    Docent("Sanne", 38, "Wiskunde"),
    Docent("Peter", 50, "Databases")
]

for docent in docenten_lijst:
    print(f"Docent {docent.naam} geeft het vak {docent.vak}.")

    print(docent)  # Print de stringrepresentatie van de docent
    