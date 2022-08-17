#!/usr/bin/env python
# coding: utf-8

# In[6]:


def binary(l1, l, h, x):
    if h>l :
        mid=(h+l)//2 
        if l1[mid]==x :
            return mid 
        elif l1[mid]>x :
            return binary(l1, l, mid - 1, x)
        else :
            return binary(l1, mid + 1, h, x)
    else :
        return -1
l1 = [ 2, 3, 4, 10, 40 ]
x = 10
r = binary(l1, 0, len(l1)-1, x)
if r !=1 :
    print(str(r))
else :
    print ("not search")
    


            


# In[8]:


def print_evennumber(x):
    if x==30 :
        return
    print(x)
    print_evennumber(x+2)
    
print_evennumber(x=0)


# In[9]:


x=0
for i in range(x,30,2) :
    print(i)


# In[ ]:




