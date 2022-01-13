#Tri rapide : Quick sort
# arr = [8,3,7,9,1,4]
import random
def generate_random_list(n,min,max):
    l = []
    for i in range(n):
        l.append(random.randint(min, max))
    return l

def qsort(l, imin, imax):
    if imax - imin == 1:
        if l[imin] > l[imax]:
            #temp = l[imin]
            #l[imin] = l[imax] 
            #l[imax] = temp
            l[imin], l[imax] = l[imax], l[imin] ## Equivaut a la permutation ci dessous
        return
    if imax-imin == 0:
        return
    pivot = l[imax]
    a = 0
    for i in range(imin, imax):
        if l[i] <= pivot:
            l[a+imin], l[i] = l[i], l[a+imin]
            a +=1
    l[a+imin],l[imax] = pivot,l[a+imin]
    if a != 0:
        qsort(l,imin,a+imin-1)
    if imax > a+imin+1:
        qsort(l,a+imin+1,imax)
def check_ordered(l):
    result = True
    for i in range (0, len(l)-1):
        if l[i] > l[i + 1]:
            result = False
    return result
list = [1,3,6,5]
l  = generate_random_list(10,0,10)
qsort(l,0,len(l)-1)
print(l) 
print(check_ordered(list))