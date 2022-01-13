def convert_str_to_int(c):
    cpt = 0
    f = 1
    for i in range(len(yes)-1,-1,-1):
        #for i in range(0,len(yes),1):
        str = yes[i]
        newStr = ord(str) - ord("0")
        nbr = newStr * f
        cpt =  nbr + cpt
        f *=10
    return cpt

def convert_str_to_int2(c):
    f = 1
    nb = 0
    for i in range(len(c)-1,-1,-1):
        n = ord(c[i]) - ord("0")
        if n < 0 or n > 9 : 
            #return None
            raise  ValueError('Cette fontion ne peut pas convertir que des chiffres')
        nb  += n * f
        f *= 10
    return nb
yes = "1906"





print(convert_str_to_int(yes))
print(convert_str_to_int2(yes))
#print(ord("1"))