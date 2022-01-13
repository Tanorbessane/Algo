#Tri par selection
l = [5,8,10,2,12]

for unsorted_index in range(0,len(l)-1):
    min = l[unsorted_index]
    min_index = unsorted_index
    for i in range(unsorted_index+1,len(l)):
        if l[i] < min:
            min = l[i]
            min_index = i
    #Permutation in-place
    l[min_index] = l[unsorted_index]
    l[unsorted_index] = min 

print(l)