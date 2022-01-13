# RAPPEL : Chaines de caractéres

a = "Tanor"
yup = "Je m'appelle Tanor BESSANE"
print(a)
print(len(a)) # pour recuperer la longuer de la chaine 
# Une chaine est indexable c'est a dire si on fait un a[0] cela affiche T exemple :  ci-dessous -1 pour recuper le dernier caractere

print(a[0])
b = a.upper()
print(b)
# SPLITT l'opperatoion inverse de slit c'est join
split_a = yup.split()
print(split_a)

noms =  ["Tanor","John","Salam","Paul"]
print("-".join(noms))