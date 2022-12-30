from class_animal import Animal
#Heritage (classe fille)
class Chien(Animal):
    #Initialisation de notre class
    def __init__(self, c_nom, c_age):
        super().__init__(c_nom, c_age)
        self.type="Chien"
        self.sound="ouaf"
    #fonction cri pour Chien
    def cri(self):
        return super().cri(self.sound)
        





