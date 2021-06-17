#!/usr/bin/env python
# coding: utf-8
Write a program to create a list of n integer values and do the following
*Add an item in to list(using function)
*Delete (using function)
*Store the largest number from the list to a variable
*Store the smallest number from the list to a variable
# In[1]:


def add(k):
    l=int(input('which position you want to add'))
    m=int(input('Enter the value of item'))
    k.insert(l,m)
    print('The new list is',k)

def dele(k):
    f=int(input('Which item you want to delete'))
    for i in range(0,len(k)):
        if k[i]==f:
            del (k[i])
    print('The new list is',k)
    
n=int(input('Enter the value of n'))
u=[]
for i in range(1,n+1):
    u.append(i)
j=int(input('Enter a number\n1.To add item in list\n2.delete from list'))
if j==1:
    add(u)
elif j==2:
    del(u)
maximum=max(u)
print(maximum)
minimum=min(u)
print(minimum)

2.Create a tuple and print reverse of the created tuple
# In[2]:


t=('mary',12,'village','machine','learning')
print(t[::-1])

3.Create a tuple and convert tuple into list
# In[3]:


t=('mary',12,'village','machine','learning')
l=print(list(t))

