#!/usr/bin/env python
# coding: utf-8

# In[1]:


True == False


# In[2]:


eng = 'kkk'
big_eng =eng.upper()
big_eng


# In[5]:


data=[]
data.append('강태규')
data.append(1)
data[:2]


# In[8]:


ban = {1:'강태규',2:'김덕민'}
ban.get(2)


# In[10]:


ban = {'강태규','김덕민'}
num = {2,3,4 '김덕민'}
ban num


# In[ ]:





# ### boolean

# In[16]:


True == False


# In[12]:


True != 0


# In[13]:


False == 0


# In[14]:


True or False


# In[15]:


1 =='1'


# ### 문자열

# In[18]:


eng = 'Korea COVID 19'
eng.lower()
eng.upper()


# ### Lists 

# In[20]:


data = []
data.append('java')
data[0],data[-1],data[1:],data[:2]
data.sort()
data.reverse()


# ### Tuple

# In[21]:


b=(1,2,3, '사','오')
c=1,2,3
type(b),type(c)
b[3] = 4
b[3:],b[1:4]


# ### Dictionay

# In[46]:


dic = {'namel':'경민','학번1':20103,'name2':'경민2','학번2':20104}
dic.get('name1')
dic.keys()
dic.values()


# ### set

# In[47]:


lunch = {'햄버거','치킨','라면','콜라',10000}
dinner = {'피자','족발','라면','콜라',10000}


# In[24]:


import pandas as pd


# In[25]:


li = [1,2,3]
li


# In[26]:


type(li)


# In[28]:


s1=pd.core.series.Series(li)
s1


# In[29]:


s2=pd.core.series.Series(['일','이','삼'])
s2


# In[30]:


pd.DataFrame(data)


# In[32]:


data=pd.DataFrame([['a',100],['b',200],['c',300]])
data.info()


# In[33]:


data.tail(1)


# In[35]:


data.tail(2)


# In[37]:


col={'1군','2군'}


# In[38]:


pd.DataFrame([['a',100],['b',200],['c',300]],columns=col)


# In[44]:


man=[
    {'Name':'은주','Age':20,'Job':'J1'},
    {'Name':'소주','Age':30,'Job':'J2'},
    {'Name':'대주','Age':40,'Job':'J3'},
]
pd.DataFrame(man, index=[1,2,3])


# In[45]:


a=[1,2,3]
b=[4,5,6]
df = [a, b]
dd=pd.DataFrame(df, index=[1,2],columns=['A','B','C'])
dd


# In[ ]:




