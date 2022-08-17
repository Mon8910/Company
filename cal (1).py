
def factorial_num(n):
    if n==0 :
        return 1 
    else :
        return n*factorial_num(n-1)
        
n=int(input("enter the number"))
print("the factorial nmber =", factorial_num(n))
def call():
    x=int(input("enter the number"))
    y=int(input("enter the number"))
    z=input("enter the operation")
    if z=='+' :
        print(x+y)
    elif z=='-' :
        print(x-y)
    elif z=='*' :
        print(x*y)
    elif z=='/' :
        print(x/y)
    else :
        print("error try again ")
    
call()






