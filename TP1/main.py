import pandas as pd
import os


#fonction pour afficher tous le personne
def Get():
    if os.path.exists('./em.csv'):
        data = pd.read_csv (r'em.csv')   
        dt = pd.DataFrame(data, columns= ['nom','prenom','age','ville'])
        print(dt)
    else:
        print("file dont exist")
#verifier si le nom exist deja
def checkexist(data):
    if os.path.exists('./em.csv'):
        mydata = pd.read_csv (r'em.csv')   
        dic=mydata.to_dict()
        for i in dic['nom']:
            if dic['nom'][i] == data['nom'][0]:
                return True
            else:
                return False
    else: return False

#ecrire dans le fichier
def write(data):
    if checkexist(data):
        print('nom existe deja')
        return Add()
    
    new = pd.DataFrame(data)
    if os.path.exists('./em.csv'):
        if os.stat('em.csv').st_size == 0:
            new.to_csv('em.csv', mode='a',header=True, index=False)
        else:
            new.to_csv('em.csv', mode='a', header=False,index=False)
    else :
        new.to_csv('em.csv', mode='a',header=True,index=False)

#fonction pour ajouter une personne
def Add():
    nom=input("entrez le nom : ")
    prenom=input("entrez le prenom : ")
    try:
        age=int(input("entrez l'age : "))
    except:
        print('age error')
        return Add()
    ville=input("entrez la ville : ")
    if not nom and not prenom and not ville :
        return print("empty input")
    if not nom.isalpha() or not prenom.isalpha() or not ville.isalpha():
        return print("you cant enter a numbre or special caracter")
    technologies = {
    'nom':[nom],
    'prenom' :[prenom],
    'age':[age],
    'ville':[ville]
        }
    write(technologies)

    

#fonction pour modifier une personne
def update():
    nom=input("merci d'entrer le nom de la personne que vous voulez modifier : ")
    mydata = pd.read_csv ('em.csv') 
    df = pd.read_csv('em.csv', index_col='nom',dtype=str)
    dic=mydata.to_dict()
    exist=False
    for i in dic['nom']:
        if dic['nom'][i] == nom:
            exist=True
            ville=''
            prenom=''
            age=0
            ville=input("entrez la ville : ")
            prenom= input("entrez le prenom : ")
            age=input("entrez l'age : ")
            if age!=0:
                try:
                    age=int(age)
                    df.loc[nom,['age']]=age
                except:
                    print('age error')
            if ville!='':
                df.loc[nom,['ville']]=ville
            if prenom!='':
                df.loc[nom,['prenom']]=prenom
            df.to_csv('em.csv')
    if not exist:
        return print ('person not exist')

#fonction pour supprimer         
def delete():
    nom =input('entrez le nom :')
    df = pd.read_csv('em.csv')
    df=df[df.nom!=nom]
    df.to_csv('em.csv',index=False)
    print('personne bien supprime')
        

#le menu de programme
n=True
while n:
    menu=input("\n1- afficher les personnne \n2- ajouter une personne \n3- modifier une personne \n4- supprimer une personne\n5- Quitter\n")
    menu = int(menu)
    if menu ==1:
        Get()
    elif menu ==2:
        Add()
    elif menu==3:
        update()
    elif menu ==4:
        delete()
    elif menu==5:
        n=False
    else:
        menu=input("\n1- afficher les personnne \n2- ajouter une personne \n3- modifier une personne \n4- supprimer une personne\n5- Quitter\n")
    



