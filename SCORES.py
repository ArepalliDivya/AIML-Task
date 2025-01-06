#!/usr/bin/env python
# coding: utf-8

# In[1]:


scores = {'virat': 90,'rohit': 100,'rahul': 60,'jadeja': 99}
scores


# In[3]:


scores["dhoni"] = 50
scores


# In[4]:


scores.setdefault("Rahul",30)
scores


# In[5]:


scores.setdefault("Pujara", 40)
scores


# In[6]:


scores.popitem()
scores


# In[7]:


scores.pop("rohit")
scores


# In[8]:


scores.get("dhoni")


# In[10]:


list1 = ["A","B","C","D"]
my_dict = dict.fromkeys(list1,20)
my_dict


# In[11]:


my_dict.update({"A":30,"B":40})
my_dict


# In[ ]:




