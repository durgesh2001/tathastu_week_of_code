n=int(input("enter a number"))

if n%2==0:                                               #to check odd/even
        print(n,"is a Even number\n")
else:
        print(n,"is a Odd number.\n")

a=2                                                      #to check prime number
while n > a:
    
    if n%a==0:
        print(n," is not a prime number.\n")
        break
    a+=1
if n==a:
    print(n," is a prime number.\n")
        
k=n                                                      #to check palindrome number
s=0
while k>0:
    rem=k%10
    s=rem+(s*10)
    k=k//10
if s==n:
    print(s,"is palindrome number\n")
else:
    print(s,"is not palindrome\n")
 
q=n                                                     #to check Amstrong number
p=0
while q>0:
    r=q%10
    p+=r**3
    q=q//10
if p==n:
    print(n," is Amstrong number.\n")
else:
    print(n," is not Amstrong number \n")
