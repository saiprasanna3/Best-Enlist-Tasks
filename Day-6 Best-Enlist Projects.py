#!/usr/bin/env python
# coding: utf-8
1.Write a Python script to merge two Python dictionaries 
# In[1]:


dict1={'places':'special','country':'currency'}
dict2={'a':100,'b':456}
d=dict1.copy() 
d.update(dict2)
print(d)

2.Write a Python program to remove a key from dictionary 
# In[2]:


dict1={'places':'special','country':'currency'}
d=dict1.pop('country')
print('The deleted element is',d)
print(dict1)

3.Write a Python program to map two lists into a dictionary
# In[3]:


keys=['name','section','branch']
values=['Sai Prasanna','A','CSE']
dict1=dict(zip(keys,values))
print(dict1)

4.Write a python program to find the length of a set 
# In[4]:


set1={2,'keys','github','linkedin','profile'}
print('The length of set is',len(set1))

5.Write a Python Program to remove the intersection of a 2nd set from the 1set

# In[5]:


set1={2,'keys','github','linkedin','profile'}
set2={'linkedin','profile'}
print('Original Sets')
print(set1)
print(set2)
for i in set1&set2:
    set1.remove(i)
    
print('set1:',set1)
print('set2:',set2)


# In[6]:


print('******************TASK COMPLETED********************')

