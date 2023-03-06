#!/usr/bin/env python
# coding: utf-8

# In[25]:


#1.	Write a Python Program to Find LCM?

def hcf(a,b):
    if a ==0:
        return b
    
    while(b):
        a,b=b,a%b
    return a

def lcm(a,b):
    lcm=(a*b)/hcf(a,b)
    print(lcm)



lcm(3,4)   


# In[17]:


#2.	Write a Python Program to Find HCF?

def hcf(a,b):
    if a ==0:
        return b
    
    while(b):
        a,b=b,a%b
    return a


    
hcf(10,5)


# In[28]:


#3.	Write a Python Program to Convert Decimal to Binary, Octal and Hexadecimal?

a=int(input())

binary=bin(a)
octal=oct(a)
hexadecimal=hex(a)
print(binary,octal,hexadecimal)


# In[31]:


#4.	Write a Python Program To Find ASCII value of a character?

a=str(input())

ASCII=ord(a)
print(ASCII)


# In[32]:


#5.	Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations?

def cal(a,b):
    return(a+b,a-b,a/b,a*b)

cal(5,10)


# In[ ]:




