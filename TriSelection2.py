## Tri par Selection
# definir une fonction qui renvoir la position de la valeur minimal de T
# Entre les position a et b

def iMin (T,a,b):
    imin = a
    N = len(T)
    for i in range(a+1, b):
        if T[i] < T[imin]:
            imin = i
    return imin
def triSelection(T):
    N = len(T)
    for i in range (N - 1):
        j = iMin(T,i,N)
        T[i],T[j] = T[j],T[i]
    return T

T = [5,8,10,2,12]

print(iMin(T,0,4))

print(triSelection(T))