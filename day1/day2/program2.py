n=int(input("enter a number."))
print("The Fibnocci series upto ",n," is")
a=0 
b=1
for i in range(n):
    print(a," ")
    c=a+b
    a=b
    b=c
