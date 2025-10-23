lst=[14,25,9,8,65,3,10]
myl=len(lst)
stin= myl-2
for i in range(stin,-1,-1):
    for j in range(0,i+1):
        if lst[j] > lst[j+1]:
            temp = lst[j] 
            lst[j] = lst[j+1]
            lst[j+1] = temp 
print(lst)