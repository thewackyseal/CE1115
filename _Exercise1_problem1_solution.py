#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Basic Libraries
import numpy as np
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt # we only need pyplot
sb.set() # set the default Seaborn style for graphics


# In[3]:


traindata = pd.read_csv('train.csv')
traindata.head()


# In[4]:


print("Data type : ", type(traindata))
print("Data dims : ", traindata.shape)


# In[5]:


print(traindata.dtypes)


# In[15]:


id = pd.DataFrame(traindata['Id'])
print("Data type : ", type(id))
print("Data dims : ", id.size)


# In[16]:


id.info()


# In[19]:


id.describe()


# In[ ]:




