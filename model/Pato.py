from interfaces.Respirar import RespirarAble
from interfaces.Terrestre import TerrestreAble
from interfaces.Volar import VolarAble
from interfaces.Nadar import NadarAble
class Elefante (RespirarAble,TerrestreAble,NadarAble,VolarAble):
    def respirar(self):
        print("el pato respira")
    def desplaza(self):
        print ("el pato se desplaza")
    def volar(self):
        print("el pato vuela")
    def nadar(self):
        print ("el pato nada")


