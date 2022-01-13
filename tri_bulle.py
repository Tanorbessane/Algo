# Tri a Bulle (Bubble sort):
#0(N^2)
import random
def generate_random_list(n,min,max):
    l = []
    for i in range(n):
        l.append(random.randint(min, max))
    return l
#________________________________________
def bubble_sort(l):
    nb_permut = 1
    while nb_permut !=0:
        nb_permut = 0
        for i in range(len(l)-1):
            if l[i] > l[i + 1]:
                nb_permut +=1
                a = l[i]
                l[i] = l[i+1]
                l[i+1] = a
l = generate_random_list(10,0,10)
bubble_sort(l)
print ("SORTED : " ,l)