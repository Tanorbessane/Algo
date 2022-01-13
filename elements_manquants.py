# les elements manquants
#Entre 1 et 10 (inclus)
# 
def elements_manquant(l, min,max):
    b=[]
    for i in range(min,max+1):
        if i not in  a :
            b.append(i)
    return b

# 2

def get_missing_numbers(l, min,max):
    return [i for i in range(min,max+1)if i not in  a]
a = [3,8,2,4,7]

print(elements_manquant(a,1,10))
print(get_missing_numbers(a,1,10))