# def func_1(n):
#     terms=[]
#     for i in range (n+1):
#         k=(3+2*i)/(2**i)
#         terms.append(k)
#     return terms
# def func_2(n):
#     terms= func_1(n)
#     s=0
#     for i in terms:
#         s=s+i
#     return s
# print(func_1(10)) 
# print(func_2(10))


# R=8.314
# def calc_mol (P,V,T):
#     n= (P*V)/(R*T)
#     return n
# print( calc_mol (5,6,10))


R= 8.314
n=1
def ideal_gas_law (P,V,T):
    if P=="?":
        P=(n*R*T)/V
        return P
    elif V=="?":
       V=(n*R*T)/P 
       return V
    else:
       T=(P*V)/(n*R)
       return T
print (ideal_gas_law("?",3,5))