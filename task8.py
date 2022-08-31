#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re 


# In[2]:


file='''
ayman mohamed kamal
mohamed ali mohamed
ali mohamed ali 

ayman.mohamed493@gmail.com
mohamed.ali4565@gmail.com
ali.lol4566@gmail.com

010-2249-2218
010-0855-0706
010-0928-6546

'''


# In[10]:


number=re.compile(r"010 /d+")
i=number.finditer(file)
phone_number=list()
for j in i :
    phone_number.append(file[j.span()[0] : j.span()[1] ] )
    
print(phone_number)    


# In[14]:


name=re.compile(r"/w+/s/w+/s/w+")
Name=name.finditer(file)
name_person=list()

for names in Name :
    name_person.append(file [names.span()[0]  : names.span() [1]   ])
print(name_person)    


# In[20]:


e-mail=re.compile(r'[a-zA-Z0-9-. + -] +@[a-zA-Z0-9-]+/.[a-zA-Z0-9-.]')
e_mail=e-mail.finditer(file)
E-mail=list()
for email in e_mail :
    E_mail.append(file[email.span()[0] :email.span() [1]])
prinr(E_mail())    


# In[ ]:





# In[ ]:




