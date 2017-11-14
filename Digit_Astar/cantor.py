import numpy as np

def fac(n):
    result = 1
    for i in range(1,n+1):
        result = result * i
    return result

def cantor_encode(n,l):
    n = len(l)
    c = [0 for i in range(n)]
    for i in range(n):
        count = 0
        for j in range(i,n):
            if l[j]>l[i]:
                count += 1
            c[n- i - 1] = count
    pos = 0
    for i in range(n):
        pos+=c[i]*fac(i)
    return pos

def cantor_decode(n,pos):
    num = [n-i-1 for i in range(n)]
    l = []
    for i in range(n-1, -1, -1):
        (quto,rem) = np.divmod(pos,fac(i))
        print(quto,rem)
        l.append(num[quto])
        num.pop(quto)
        pos = rem
    return l


'''
i = cantor_encode(5,[1,0,2,3,4])
print(i)
print(cantor_decode(5,i))
'''
