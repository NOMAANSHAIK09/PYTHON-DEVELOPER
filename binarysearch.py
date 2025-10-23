lst=[12,34,56,78,90,6]
target=56
min=0
max=len(lst)-1
for i in range(len(lst)):
    mid=(min+max)//2
    print(mid)
    if lst[mid]==target:
        print(f"found {target}")