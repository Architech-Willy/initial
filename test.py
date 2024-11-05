def twosum (L,target):
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            if L[i]+L[j] == target:
                return i,j
            

print(twosum([2,7,11,15],9))