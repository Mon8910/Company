#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Bankaccount :
    def __init__(self):
        print("welcome to bank")
        self.name=input("please enter your name : ")
        self._id=int(input("enter your id :"))
        self._password=int(input("enter your password :"))
        self.phone=int(input("enter your phone :"))
        self._credit=0
    def dispossed(self):
        d=float(input("enter your despost"))
        self._credit=self._credit+d
    
    
    def checkpass(self):
        dd=int(input("enter your password"))
        if dd==self._password :
            print("your credit",self._credit)
        else :
            print("error")
    def fastdesp(self):
        
        de=float(input("enter your despost"))
        self._credit=de+self._credit
        print("show my credit",self._credit)
        
        
    def withdraw(self):
        w=float(input("enter your withdraw"))
        
        if self._credit-w <0 :
            
            print("error")
        else :
            self._credit=self._credit-w
            print("this is completed =",self._credit)
    def FDass(self):
        nNid=int(input("enter your id :"))
        if nNid == self._id :
            passs=int(input("enter your new password :"))
        else :
            print("error ")


# In[2]:


a=Bankaccount()


# In[ ]:




