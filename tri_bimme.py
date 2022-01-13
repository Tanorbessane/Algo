# Tri a Bulle (Bubble sort):
#0(N^2)

l = [4,8,7,2]

def bulle_sort(l):
    cpt_permutation = 1
    while cpt_permutation != 0:
        cpt_permutation = 0
        min = l[0]
        for i in range(0,len(l)-1):
            j = i + 1
            if l[i] > l[j] :
                temp = l[j]
                l[j] = l[i]
                l[i] = temp
                cpt_permutation +=1

    return l

print(bulle_sort(l))
