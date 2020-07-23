#!/usr/bin/env python
# coding: utf-8

# In[48]:


n=int(input("enter n: "))
c=0
for i in range(2,n,1):
    if n%i==0:
        c=c+1
if c==0:
    print("prime number")
else:
    print("not prime number")


# In[46]:


sum=0
i=0
while i<10:
    sum =sum + i
    print(sum)
    i=i+1


# In[ ]:




