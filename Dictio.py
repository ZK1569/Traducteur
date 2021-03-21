import os 
from Fonctions import *

change = True 


while change :
    
    langue = input("Quelle langue voulez-vous utiliser = ")
    
    if langue == "francais":
        exe(fr_an)
                
    elif langue == 'anglais':
        exe(an_fr)
    
    else:
        print("Recommence")
        continue
    
    
    recommence = input("Changer de langue ? (oui/non) ")
    if recommence == "non":
        change = False
    
os.system("pause")
    

