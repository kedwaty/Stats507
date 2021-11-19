#!/usr/bin/env python
# coding: utf-8

# ### youngwoo Kwon
# 
# kedwaty@umich.edu

# # Question 0 - Topics in Pandas

# In[1]:


import pandas as pd
import numpy as np
import scipy.stats as stats
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import time


# ## Missing Data in Pandas 
# 
# Pandas is very __flexible__ to the missing values
# 
# * NaN is the default missing value
# 
# * However, we should deal with the different types such as integer, boolean, or general object.
# 
# * We should also consider that "missing" or "not available" or "NA".

# ## Detecting the Missing Values
# 
# * Pandas provides `isna()` and `notna()` function to detect the missing values

# In[2]:


df = pd.DataFrame(
    np.random.randn(4, 3),
    index=["a", "c", "e", "f"],
    columns=["one", "two", "three"],
)
df["five"] = df["one"] < 0
df2 = df.reindex(["a", "b", "c", "d", "e"])
df2


# In[3]:


df2.isna()


# In[4]:


df2.notna()


# ## More about the Missing Values
# 
# * In Python, nan's don't compare equal, but None's do.
# 
# * NaN is a float, but pandas provides a nullable integer array

# In[5]:


None == None


# In[6]:


np.nan == np.nan


# In[7]:


print(df2.iloc[1,1])
print(type(df2.iloc[1,1]))


# In[8]:


pd.Series([1, 2, np.nan, 4], dtype=pd.Int64Dtype())

