ls1 = []
ls2 = []
massiv = []
for i in range(0, len(ls1)):
    for j in range(0, len(ls2)):
        if i == j:
#            print(ls1[i])
 #           print(ls2[j])
            c = ls1[i] + ls2[j]
            massiv.append(c)
print(massiv)
