# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.12.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# + [markdown] slideshow={"slide_type": "slide"}
# ## **Name**  : *Xin Luo*
# ## **EMAIL**  :  *luosanj@umich.edu*

# + [markdown] slideshow={"slide_type": "slide"}
# #  Question 0
#
# ##  Pandas .interpolate() method
#
# * Method *interpolate* is very useful to fill NaN values.
# * By default, NaN values can be filled by other values with the same index for different methods.
# * Please note that NaN values in DataFrame/Series with MultiIndex can be filled by 'linear' method as
# <code>method = 'linear' </code>. 

# + slideshow={"slide_type": "subslide"}
import pandas as pd
import numpy as np
a = pd.DataFrame({'a' : [1, 2, np.nan, 5], 'b' : [4, np.nan, 6, 8]})
a.interpolate(method = 'linear')

# + [markdown] slideshow={"slide_type": "slide"}
# ### Parameters in .interpolate()
# ##### *parameter **'method'** : *str*, default *'linear'
#
#
# * Most commonly used methods:
#     * 1. **'linear'** : linear regression mind to fit the missing ones.
#     * 2. **'pad', 'limit'** :  Fill in NaNs using existing values. Note:Interpolation through padding means copying the value just before a missing entry.While using padding interpolation, you need to specify a limit. The limit is the maximum number of nans the method can fill consecutively.
#     * 3. **'polynomial', 'order'** : Polynomial regression mind with a set order to fit the missing ones. Note : NaN of the first column remains, because there is no entry before it to use for interpolation.

# + slideshow={"slide_type": "subslide"}
m =  pd.Series([0, 1, np.nan, np.nan, 3, 5, 8])
m.interpolate(method = 'pad', limit = 2)

# + slideshow={"slide_type": "subslide"}
n = pd.Series([10, 2, np.nan, 4, np.nan, 3, 2, 6]) 
n.interpolate(method = 'polynomial', order = 2)

# + [markdown] slideshow={"slide_type": "slide"}
# ##### parameter **'axis'** :  default *None*
# * 1. axis = 0 : Axis to interpolate along is index.
# * 2. axis = 1 : Axis to interpolate along is column.
#     

# + slideshow={"slide_type": "subslide"}
k = pd.DataFrame({'a' : [1, 2, np.nan, 5], 'b' : [4, np.nan, 6, 8]})
k.interpolate(method = 'linear', axis = 0)
k.interpolate(method = 'linear', axis = 1)

# + [markdown] slideshow={"slide_type": "slide"}
# ###  Returns
# * Series or DataFrame or None
# * Returns the same object type as the caller, interpolated at some or all NaN values or None if `inplace=True`.
# -

# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     notebook_metadata_filter: markdown
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.13.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# ## Topics in Pandas
# **Stats 507, Fall 2021** 
#   

# ## Contents
#
# + [DateTime in Pandas](#DateTime-in-Pandas) 
# + [Create DatetimeIndex](#Create-DatetimeIndex) 
# + [Convert from other types](#Convert-from-other-types) 
# + [Indexing with DatetimeIndex](#Indexing-with-DatetimeIndex) 
# + [Date/time components in the DatetimeIndex](#Date/time-components-in-the-DatetimeIndex) 
# + [Operations on Datetime](#Operations-on-Datetime) 

# ## DateTime in Pandas
#
# *Qi, Bingnan*
# bingnanq@umich.edu
#
# - Pandas contains a collection of functions and features to deal with time series data. A most commonly used class is `DatetimeIndex`.
#

# ## Create DatetimeIndex
#
# - A `DatetimeIndex` array can be created using `pd.date_range()` function. The `start` and `end` parameter can control the start and end of the range and `freq` can be `D` (day), `M` (month), `H` (hour) and other common frequencies.

pd.date_range(start='2020-01-01', end='2020-01-05', freq='D')

pd.date_range(start='2020-01-01', end='2021-01-01', freq='2M')

# ## Convert from other types
#
# - Other list-like objects like strings can also be easily converted to a pandas `DatetimeIndex` using `to_datetime` function. This function can infer the format of the string and convert automatically.

pd.to_datetime(["2020-01-01", "2020-01-03", "2020-01-05"])

# - A `format` keyword argument can be passed to ensure specific parsing.

pd.to_datetime(["2020/01/01", "2020/01/03", "2020/01/05"], format="%Y/%m/%d")

# ## Indexing with DatetimeIndex
#
# - One of the main advantage of using the `DatetimeIndex` is to make index a time series a lot easier. For example, we can use common date string to directly index a part of the time series.

# +
idx = pd.date_range('2000-01-01', '2021-12-31', freq="M")
ts = pd.Series(np.random.randn(len(idx)), index=idx)

ts['2018-09':'2019-04']
# -

ts['2021-6':]

# ## Date/time components in the DatetimeIndex
#
# - The properties of a date, e.g. `year`, `month`, `day_of_week`, `is_month_end` can be easily obtained from the `DatetimeIndex`.

idx.isocalendar()

# ## Operations on Datetime
#
# - We can shift a DatetimeIndex by adding or substracting a `DateOffset`

idx[:5] + pd.offsets.Day(2)

idx[:5] + pd.offsets.Minute(1)


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
