class Animal():
     #Initialisation de notre class
     def __init__(self, c_nom, c_age):
         self.nom = c_nom
         self.age = c_age
         
    #fonction cri animal
     def cri(self, message):
         print("Le cri de {} : {}".format(self.nom, message))
         



