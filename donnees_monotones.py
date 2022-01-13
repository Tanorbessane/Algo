def is_increasing_monotonic_values(l):
    for i in range(len(l)-1):
        if l[i+1] < l[i]:
            return False
    return True

def is_increasing_monotonic_values_2(l):
    l_sort = sorted(l)
    return l == l_sort
a = [1,2,4,6,8,10,11, 11,12]
b = [1,2,5,6,2,10,11, 11,12]
print(is_increasing_monotonic_values_2(a))
