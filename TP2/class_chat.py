from class_animal import Animal
#Heritage (classe fille)
class Chat(Animal):
     #Initialisation de notre class
     def __init__(self, c_nom, c_age):
          super().__init__(c_nom,c_age)
          self.type="Chat"
          self.sound="Miaou"
     
     #fonction cri pour Chat
     def cri(self):
          return super().cri(self.sound)
        



