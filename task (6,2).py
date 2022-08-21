#!/usr/bin/env python
# coding: utf-8

# In[28]:


class Bankaccount :
    def __init__(self):
        print("welcome to bank")
        self.name=input("please enter your name : ")
        self.__id=int(input("enter your id :"))
        self.__password=int(input("enter your password :"))
        self.phone=int(input("enter your phone :"))
        self._credit=0 #protected  to accsess to any class
    def dispossed(self):
        d=float(input("enter your despost"))
        self._credit=self._credit+d
    
    
    def checkpass(self):
        dd=int(input("enter your password"))
        if dd==self.__password :
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


# In[29]:


class Ahlybank(Bankaccount):
    def Digital(self):
        self.__wdd=int(input("enter your pass"))
        self.__digitalwa=0
    def mm(self):
        od=int(input("enter ur pass to check"))
        if od == self.__wdd :
            amount=float(input("enter ur amount"))
            self.__digitalwa+=amount
            print(self.__digitalwa)
        
    def ccredit(self) :
        print(self.__digitalwa+self._credit)
    
    


# In[30]:


a=Ahlybank()


# In[31]:


a.fastdesp()


# In[32]:


a.Digital()


# In[33]:


a.mm()


# In[34]:


a.ccredit()


# In[ ]:




