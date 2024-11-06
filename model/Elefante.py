from interfaces.Respirar import RespirarAble
from interfaces.Terrestre import TerrestreAble

class Elefante (RespirarAble,TerrestreAble):
    def respirar(self):
        print("el elefante respira")
    def desplaza(self):
        print ("el elefante se desplaza")