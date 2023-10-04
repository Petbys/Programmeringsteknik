''' Avrundar listan elementvis '''

def round_list(a_list, ndigits):
    ny=[]
    ny=[round(e,ndigits) for e in a_list]
#   for i in range(0,len(a_list)):
#       a_listny.append(round(a_list[i],ndigits))
    return ny


x=[1.0, 0.0, 0.0, 0.0, 1.6666666666666667, 3.3333333333333335, 6.0, 6.666666666666667]
print(round_list(x,2))