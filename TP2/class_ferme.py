#coding:utf-8
from utils import *

class Ferme():
     #Initialisation de notre class
     def __init__(self):
          self.animaux=[]
         
     #fonction pour ajouter un animal
     def ajouter_animal(self, add):
          print("le {} {} est ne".format(add.type, add.nom))
          self.animaux.append(add)
     
     #fonction pour lancer le cri de tous les animaux de la ferme
     def crier(self):
          for i in self.animaux:
               i.cri()

     #fonction pour tuer un animal
     def tuer(self,nom):
          exist=False
          for i in self.animaux:
               if i.nom==nom:
                    self.animaux.remove(i)
                    print("le {} {} est mort".format(i.type, i.nom))
                    exist=True
          return exist
     #fonction pour voir le nombre des animaux dans la ferme
     def __str__(self) -> str:
          return f'Ma ferme a {len(self.animaux)} animaux'
               
         

#creer noter ferme
f1 = Ferme()

#le menu de programme
n=True
while n:
     menu=input("\n1- Ajouter un animal \n2- Lancer le cri de tous les animaux de la ferme. \n3- Tuer un animal \n4- consulter la ferme\n5- Quitter le programme\n")
     menu = int(menu)
     if menu ==1:
        ajouter(f1)
     elif menu ==2:
        Crier(f1)
     elif menu==3:
        Tuer(f1)
     elif menu ==4:
        nombre(f1)
     elif menu==5:
          n=False
     else:
          menu=input("\n1- Ajouter un animal \n2- Lancer le cri de tous les animaux de la ferme. \n3- Tuer un animal \n4- consulter la ferme\n5- Quitter le programme\n")
