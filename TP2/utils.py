from class_chat import Chat
from class_chien import Chien

#fonction pour ajouter un animal
def ajouter(ferme):
    print("choisez le type d'animal")
    type=int(input("1 - Chat\n2 - Chien\n"))
    nom=input('entrez le nom : ')
    try:
        age=int(input("entrez l'age : "))
    except:
        print("age error")
        return ajouter(ferme)
    if type==1:
        ferme.ajouter_animal(Chat(nom,age))
    elif type==2:
        ferme.ajouter_animal(Chien(nom,age))
    else:
        print('type error')
        return ajouter(ferme)

#fonction pour lancer le cri des animaux
def Crier(ferme):
    ferme.crier()

#fonction pour tuer un animal
def Tuer(ferme):
    nom=input("entrez le nom de l'animal : ")
    if not ferme.tuer(nom):
        print("animal dont exist")
        
#fonction pour consulter le nombre des animaux dans la ferme
def nombre(ferme):
    print(ferme.__str__())