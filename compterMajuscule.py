def compterMajuscule(string):
    cpt = 0
    for i in range(len(string)):
        if string[i].isupper():
            cpt +=  1        
    print("Le nombre de majuscule est  ",cpt)

def count_upper_characters(string):
    count = 0
    for c in string:
        if c.isupper():
            count +=1
    return count
def count_upper_characters2(string):
    l = [1  for c in string if c.isupper()]
    return len(l)
Chaine = "BonJouOO la vie"
compterMajuscule(Chaine)
print (count_upper_characters(Chaine))
print (count_upper_characters2(Chaine))