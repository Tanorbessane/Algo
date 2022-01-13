# RAPPEL : Dictionnaire
# clé ==> valeur
p = {"nom": "Tanor", "age":27}
print(p["nom"])
age = p.get("age")
if age:
    print("Age de la personne "+ str(age))
else:
    print("L'age n'est pas specificie ")

# Les dictionnaires servent à structurer les données, soit pour à faire des algos plus puissant
repertoire = {"Tanor Bessane" : {"age":20,"tel":"0617527710"},
               "Marie Dupot" : {"age":30,"tel":"0617237710"},
                "Amina Seye" : {"age":25,"tel":"0717237710"}
}

personne_recherchee = "Tanor BESSANE"
info = repertoire["Tanor Bessane"]
#print(info)
for element in repertoire:
    print(element)
print(' '.join(format(ord(x),'b') for x in element))