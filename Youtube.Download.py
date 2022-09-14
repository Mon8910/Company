#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pytube


# In[4]:


url_link=input("please enter ur link to downlaod")
pytube.YouTube(url_link).streams.get_highest_resolution().download('Desktop')


# In[ ]:




