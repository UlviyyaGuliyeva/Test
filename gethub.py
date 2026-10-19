R=8.314
def calc_mol (P,V,T):
    n= (P*V)/(R*T)
    return n
print( calc_mol (5,6,10))
