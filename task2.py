#!/usr/bin/env python
# coding: utf-8

# In[1]:


for i in range (1500,2701):
    if (i%7==0) and (i%5==0):
      
        print (i)


# In[2]:


c=float(input("enter the celsius "))
f=float(input("enter the fahrenheit"))
m= c/5
n= (f-32)/9
print("fahrenheit= ",m)
print("celsius= ",n)


# In[3]:


n=5 
for i in range(n):
    for j in range(i+1):
    
        print("*",end="")
    print()
for i in range(n):
    for j in range(i,n):
        print("*",end="")
    print()


# In[4]:


word=input("enter the word ")
print("accepts a word = ",word )
for i in range(len(word)-1,-1,-1):
    print(word[i], end="")
print("\n")


# In[6]:


def max_number() :
    n1=int(input("enter the first number "))
    n2=int(input("enter the second number "))
    n3=int(input("enter the third number"))
    if n1>=n2 and n1>n3 :
        print("the max numer is =",n1)
    elif n2>n1 and n2>n3 :
        print("the max number is = ",n2 )
    elif n3>n1 and n3>n2 :
        print("the max number is =",n3)
    else :
        print("n1=n2=n3")
max_number()        


# In[7]:


def sum_list() :
    l1=[10,25,30,40]
    print(sum(l1))
sum_list()


# In[8]:


for i in range(6):
    if i==3 or i==6 :
        continue
    print(i)


# In[9]:



def factorial_num(n):
    if n==0 :
        return 1 
    else :
        return n*factorial_num(n-1)
        
n=int(input("enter the number"))
print("the factorial nmber =", factorial_num(n))


# In[11]:


def unique_list(l):
  x = []
  for a in l:
    if a not in x:
      x.append(a)
  return x

print(unique_list([1,2,3,3,3,3,4,5]))


# In[ ]:


#i can't understand Lambda function 

