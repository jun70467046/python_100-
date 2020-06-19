#!/usr/bin/env python
# coding: utf-8

# ### 여러개의 파일 가져오기

# In[19]:


import pandas as pd


# In[20]:


path=r'C:\Users\user\Desktop\새 폴더\score\A.csv'


# In[21]:


path


# In[22]:


pd.read_csv(path, encoding='cp949')


# In[24]:


import glob


# In[25]:


data=r'C:\Users\user\Desktop\새 폴더\score\\'


# In[42]:


stu=[]
for file in glob.glob(data+'*.csv'):
    #print(file)
    data_stu = pd.read_csv(file, encoding='cp949')
    stu.append(data_stu)


# In[43]:


stu


# In[27]:


a=[]


# In[28]:


a


# In[32]:


a.append(3)


# In[33]:


a


# In[34]:


a.append(10)


# In[35]:


a


# In[36]:


stu=[]


# In[37]:


stu


# In[ ]:


data_stu = pd.read_csv(file, encoding='cp949')
stu.append(file)

