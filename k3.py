import sys, string, math
k1,k2 = input().split()
n1 = len(k1)
n2 = len(k2)
if n2 > n1 :
    i = 0
    while i<n1 and k1[i] == k2[i] :
        i += 1
    print(n2-i)
elif n2 == n1 :
    i = 0
    while i<n2 and k1[i] == k2[i] :
        i += 1
    print(n2-i)
else :
    i = 0
    while i<n2 and k1[i] == k2[i] :
        i += 1
    s31 = k1[i:]
    s32 = k2[i:]
    L = list(s31)
    k = 0
    for c in s32 :
        if c in L :
            k += 1
            L.remove(c)
    print(n1-i-k)
