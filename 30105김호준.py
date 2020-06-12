#!/usr/bin/env python
# coding: utf-8

# In[1]:


import turtle as t


# In[26]:


t.shape('turtle')
t.color('red', 'yellow')
t.begin_fill()
t.fd(200)
t.left(120)
t.fd(200)
t.left(120)
t.fd(200)
t.end_fill()
t.exitonclick()


# In[29]:


from turtle import *
color('red', 'yellow')
begin_fill()
while True:
    forward(200)
    left(170)
    if abs(pos()) < 1:
        break
end_fill()
done()


# In[ ]:


import turtle as t
t.shape('turtle')
t.fd(200)
t.left(144)
t.fd(200)
t.left(144)
t.fd(200)
t.left(144)
t.fd(200)
t.left(144)
t.fd(200)
t.exitonclick()


# In[24]:


import turtle as t
t.shape('turtle')
t.color('red', 'yellow')
t.begin_fill()

n = int(input('몇각형???'))
for i in range(n):
    for i in range(n):
        t.fd(200)
        t.left(300/n)   
    t.right(150)    
t.end_fill()
t.exitonclick()

