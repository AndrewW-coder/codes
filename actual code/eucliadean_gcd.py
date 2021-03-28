def egcd2(n1, n2):
    l = [n1, n2]
    if (max(l)/min(l)).is_integer() == True:
        return min(l)
    return egcd2(min(l), max(l) % min(l))

print(egcd2(84, 15))