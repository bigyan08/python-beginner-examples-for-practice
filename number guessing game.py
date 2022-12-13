import random
a=random.randint(1,6)
print("check your instinct\n")
b=input("guess the number:\n")
print(a)
if int(a)==int(b):
    print("correct")
else:
    print("incorrect")