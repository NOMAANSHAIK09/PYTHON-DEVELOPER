x=int(input("enter the digit:"))
xcpy=x
sum=sumeven=sumodd=0
while x>0:
    rem=x%10
    print("extracted number is:",rem)
    if rem % 2 == 0:
       sumeven = sumeven + rem
    else:
       sumodd = sumodd + rem
    x = x//10
else:
    print("the sum of even in ",xcpy, "is",sumeven)
    print("the sum of odd in ",xcpy ,"is",sumodd)