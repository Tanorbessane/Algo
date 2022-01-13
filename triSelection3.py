#Tri par selection
import random
l = [5,8,1,4]
print("UNSORTED : ",l)
for unsorted_index in range(0,len(l)-1):
    min = l[unsorted_index]
    min_index = unsorted_index
    for i in range(unsorted_index+1,len(l)):
        if l[i] < min:
            min = l[i]
            min_index = i
    #In place : 
    l[min_index] = l[unsorted_index]
    l[unsorted_index] = min
print("SORTED : ",l)

# Creer une fonction generate_random_list(n,min,max) qui va generer des listes de facon aleatoire
# Mettre lalgo de trie par selection dans une fonction select_sort(l)

def generate_random_list(n,min,max):
    l = []
    for i in range(n):
        l.append(random.randint(min, max))
    return l

L = generate_random_list(10,2,9)
def select_sort(l):
    print ("UNSORTED : " ,l)
    for unsorted_index in range(0,len(l)-1):
        min = l[unsorted_index]
        min_index = unsorted_index
        for i in range(unsorted_index+1,len(l)):
            if l[i] < min:
                min = l[i]
                min_index = i
        #In place : 
        l[min_index] = l[unsorted_index]
        l[unsorted_index] = min
    print("SORTED : ",l)

select_sort(L)