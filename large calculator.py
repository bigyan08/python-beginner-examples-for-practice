print("WELCOME\n")
c=0
b=int()
a=input("PLEASE SPECIFY THE TYPE OF CALCULATION\n enter S for sum \n enter D for division \n enter SU for subtraction \n enter M for multiplication\n")
if str(a)=="S":
    x=input("ENTER THE 1st NUMBER\n")
    y=input("ENTER THE 2nd NUMBER\n")
    print(int(x) + int(y))

elif str(a)=="D":
    x = input("ENTER THE DIVIDEND\n")
    y = input("ENTER THE DIVIDER\n")
    print(int(x) / int(y))

elif str(a)=="SU":
    x = input("ENTER THE 1st NUMBER\n")
    y = input("ENTER THE 2nd NUMBER\n")
    print(int(x) - int(y))

elif str(a)=="M":
    x = input("ENTER THE 1st NUMBER\n")
    y = input("ENTER THE 2nd NUMBER\n")
    print(int(x) * int(y))
