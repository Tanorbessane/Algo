#RAPPEL : Les Fonctions

def demander_nom():
    response = ""
    response = input("Quel est votre nom ? ")
    if response == "":
        print("ERROR: Le nom ne doit pas etre vide !!!")
        return demander_nom() # Recursion c'est d'appeler la fonction elle meme 
    return response


def afficher_nom(nom=""): #Pour rendre un paramettre optionnel il faut le donner une valeur par defaut
    if(nom == ""):
        print("Le nom est vide ")
        return
    print("Je m'appelle Tanor BESSANE")
    print("Allias "+nom)

nom_de_la_personne= demander_nom()
afficher_nom(nom_de_la_personne)