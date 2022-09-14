#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import requests
from bs4 import BeautifulSoup


# In[3]:


website=requests.get("https://coreyms.com/page/3").text
website


# In[5]:


soup=BeautifulSoup(website,'lxml')
print(soup.prettify())


# In[10]:


csvfile=open('scrape88.csv','w',encoding='utf-8')
writer=csv.writer(csvfile)
writer.writerow(['head','paragragh'])


# In[15]:


articles=soup.find_all("article")
for i in articles :
    head=i.header.h2.a.text
    print(head)
    paragragh=i.find('div',class_="entry-content").p.text
    print(paragragh)
    writer.writerow([ head,paragragh])
csvfile.close()    


# In[ ]:




