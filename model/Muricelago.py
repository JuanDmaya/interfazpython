from interfaces.Respirar import RespirarAble
from interfaces.Volar import VolarAble

class Muricelago (RespirarAble,VolarAble):
    def respirar(self):
        print("el murcielago respira")
    def volar(self):
        print ("el murcielago vuela")