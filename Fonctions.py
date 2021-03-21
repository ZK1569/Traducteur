import pickle
import os

test = {"hello":"Bonjour"}

fr_an = "fichier_fr_an"
an_fr = "fichier_an_fr"

def save(fichier, mots_trad):
    with open(fichier,"wb") as f:
        variable = pickle.Pickler(f)
        variable.dump(mots_trad)
       
def down_save(fichier):
    with open(fichier,'rb') as f:
        mon_pickler = pickle.Unpickler(f)
        dictio = mon_pickler.load()
        return dictio
    
def trad(langue):
    print("-------Traduction--------")
    f = down_save(langue)
    mots = input("Mot a traduire = ")
    if mots not in f:
        print("Le mot n'est pas dans la liste")
    else:
        print (mots ,"=>", f[mots])

def ajoute(langue):
    print("---------Ajouter---------")
    f = down_save(langue)
    mots = input("Mot as ajouter = ")
    trad = input("Mot traduit = ")
    f[mots] = trad
    save(langue,f)
    print ("OK")

def sup(langue):
    print("--------Supprimer---------")
    f = down_save(langue)
    sup = input("Mot a supprimer = ")
    if sup not in f:
        print ("Le mot n'est pas dans la liste")
    else:
        ca_trad = f.pop(sup)
        save(langue,f)
        print ("{} et {} sont suppriés".format(sup, ca_trad))
 
def afficher(langue):
    print("------Afficher------")
    f = down_save(langue)
    print (f)
    
def exe(langue):
    rep_while = True 
    while rep_while : 
        suite = input("Que faire ? (traduire / ajouter / supprimer / afficher) ")
        if suite == "traduire":
            trad(langue)
        elif suite == "ajouter":
            ajoute(langue)
        elif suite == "supprimer":
            sup(langue)
        elif suite == "afficher":
            afficher(langue)
        else:
            print ("Recommence")
            continue
        continu = input("Recommencer ? (oui/non) ")
        if continu != "oui":
            rep_while = False
   
    
    
    
    



