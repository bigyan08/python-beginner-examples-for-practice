a=int(input("enter any number\n"))
c=0
for x in range(1,int(a)):
    r= a % x
    x=x+1
    if int(r)==0:
        c=c+1
if c==1:
    print("prime")
else:
    print("composite")



