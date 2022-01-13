import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

l = int(input())
h = int(input())
t = input()
rows = []
for i in range(h):
    rows.append(input())

t = t.upper()
for j in range(len(rows)):
    ligne = ""
    for i in range (len(t)):
        c = t[i]
        if ord(c) < ord("A") or ord(c) > ord("Z"):
            # Caractere special
            index = 26
        else : 
            index = ord(c) - ord("A")
        ex = rows[j][index*l:(index+1)*l]
        ligne += ex
    print(ligne)
    #print(' '.join(format("C",'b')))

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

#print("answer")
