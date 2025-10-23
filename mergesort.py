lst1=[2,3,5,15,25]
lst2=[1,7,17,20,30,35,4]
lstres=[]
i=j=0
while i < len(lst1) and j < len(lst2):
    if lst1[i] > lst2[j]:
        lstres.append(lst2[j])
        j+=1
        print(lstres)
    else:
        lstres.append(lst1[i])
        i+=1
        print(lstres)
while j < len(lst2):
    lstres.append(lst2[j])
    j+=1
    print(lstres)
while i < len(lst1):
    lstres.append(lst1[i])
    i+=1
    print(lstres)
    print(lstres)