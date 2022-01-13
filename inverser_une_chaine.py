def reverse_string(string):
    str_rvs = ""
    i = len(string)
    while i > 0:
        str_rvs = str_rvs + string[i-1]
        i = i - 1
    return str_rvs
# Methode Boucle for

def reverse_string_for(string):
    r = ""
    for i in string:
        r = i + r
    return r
def reverse_string_slice(string):
    return string[::-1]
s = "Bonjour toto"
yes = reverse_string(s)
print(reverse_string_for(s))
print(yes)

