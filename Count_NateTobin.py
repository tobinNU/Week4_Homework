#!/usr/bin/env python
# coding: utf-8

# In[1]:


def count(word, letter):
    count = 0
    for l in word:
        if letter == l:
            count = count + 1
    return count


# In[2]:


count('banana', 'a')


# In[3]:


count('banana', 'n')


# In[4]:


count('banana', 'b')


# In[ ]:




