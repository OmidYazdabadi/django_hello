class Motor:
    def __init__(self, brandstof, vermogen):
        self.vermogen = vermogen
        self.brandstof = brandstof

class Benzinemotor(Motor):
    def __init__(self):
        super().__init__(150, "benzine")

class Auto:
    def __init__(self, motor, merk):
        self.motor = motor
        self.merk = merk

auto = Auto(Benzinemotor(), "BMW")

print(auto.motor.brandstof)