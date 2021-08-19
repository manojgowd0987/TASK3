#!/usr/bin/env python
# coding: utf-8

# # The Sparks Foundation- GRIP- Data Science and Buisness Analytics- Aug-2021

# # Task 3:- Exploratory Data Analysis - Retail

# # Author :- MANOJ GOWD

# # Dataset can downloaded from this link:-https://bit.ly/3i4rbWl

# # Problem Statement:
# 

# # As a business manager, try to find out the weak areas where you can work to make more profit.

# # Importing the Libaries

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import warnings
import seaborn as se
warnings.filterwarnings("ignore")

get_ipython().run_line_magic('matplotlib', 'inline')


# 
# 
# *   Lets Import our data
# *   Let's get understanding what our data is about
# 
# 
# 
# 
# 

# # Importing the Dataset

# In[2]:


df=pd.read_csv("SampleSuperstore.csv")
df


# # **Let"s Explore our Data**

# In[3]:


df.head()


# In[4]:


df.tail()


# In[5]:


df.info()


# In[6]:


df.describe()


# In[7]:


df.shape


# In[8]:


df.isnull().sum()


# In[9]:


df.corr()


# # Checking the Unique values in Required columns

# In[10]:


df['Ship Mode'].unique()


# In[11]:


df['Segment'].unique()


# In[12]:


df['Country'].unique()


# In[13]:


df['City'].unique()


# In[14]:


df['State'].unique()


# In[15]:


df['Category'].unique()


# In[16]:


df['Region'].unique()


# # Visulazing the data

# In[17]:


se.pairplot(df)


# In[18]:


se.boxplot(df['Sales'])


# In[19]:


se.boxplot(df['Discount'])


# In[20]:


se.boxplot(df['Profit'])


# In[21]:


df.drop_duplicates(subset = None , keep ='first', inplace = True)


# In[22]:


df.duplicated().sum()


# In[23]:


se.heatmap(df.corr(),cmap = "YlGnBu",annot = True)


# We infer that:
# 
# 
# 
# 
# *   Sales and profit have a direct relationship
# 
# *    Sales and Disount have an inverse relationship
# 
# *    Quantity and profit have some kind of a positive proportionality
# 
# *    Profit and Disount have an inverse relationship
# 
# 
# 

# In[24]:


x, y = plt.subplots(nrows = 2 , ncols = 2 , figsize=(15,7))
se.countplot(df['Ship Mode'],ax = y[0][0])
se.countplot(df['Segment'],ax = y[0][1])
se.countplot(df['Region'],ax = y[1][0])
se.countplot(df['Category'],ax = y[1][1])
y[0][0].set_title("Ship Mode",fontsize = 20)
y[0][1].set_title("Segment",fontsize = 20)
y[1][0].set_title("Region",fontsize = 20)
y[1][1].set_title("Category",fontsize = 20)
plt.tight_layout()


# In[25]:


x, y  = plt.subplots(figsize=(10,6))
se.countplot(df['Sub-Category'],x=x)
plt.title("Sub-Category",fontsize=25)
plt.xticks(rotation=90)


# In[26]:


x, y  = plt.subplots(figsize=(10,6))
se.countplot(df['Category'],x=x)
plt.title("Category",fontsize=25)
plt.xticks(rotation=90)


# In[27]:


x1 = df['State'].value_counts()
x1 = x1.head(10)
x1.plot(kind = "bar",figsize=(10,6))
plt.ylabel("Numbers")
plt.xlabel("State")
plt.title("States with Top Sales")


# In[28]:


x1 = df['City'].value_counts()
x1 = x1.head(10)
x1.plot(kind = "bar",figsize=(10,6))
plt.ylabel("Numbers")
plt.xlabel("Cities")
plt.title("City with Top Sales")


# ## ***Profits , Discounts and sales based on Shop mode***

# In[29]:


x ,y = plt.subplots(figsize=(10,6))
se.barplot(df['Ship Mode'],df['Profit'],y = y)


# In[30]:


x ,y = plt.subplots(figsize=(10,6))
se.barplot(df['Ship Mode'],df['Sales'],y = y)


# In[31]:


x ,y = plt.subplots(figsize=(10,6))
se.barplot(df['Ship Mode'],df['Discount'],y = y)


# In[32]:


x ,y = plt.subplots(figsize=(10,6))
se.barplot(df['Segment'],df['Profit'],y = y)


# In[33]:


x ,y = plt.subplots(figsize=(10,6))
se.barplot(df['Segment'],df['Discount'],y = y)


# In[34]:


x ,y = plt.subplots(figsize=(10,6))
se.barplot(df['Segment'],df['Sales'],y = y)


# In[35]:


x ,y = plt.subplots(figsize=(10,6))
se.barplot(df['Segment'],df['Discount'],y = y)


# In[36]:


x ,y = plt.subplots(figsize=(10,6))
se.barplot(df['Region'],df['Profit'],y = y)


# In[37]:


x ,y = plt.subplots(figsize=(10,6))
se.barplot(df['Region'],df['Sales'],y = y)


# In[38]:


x ,y = plt.subplots(figsize=(10,6))
se.barplot(df['Region'],df['Discount'],y = y)


# In[39]:


x ,y = plt.subplots(figsize=(10,6))
se.barplot(df['Category'],df['Sales'],y = y)


# In[40]:


x ,y = plt.subplots(figsize=(10,6))
se.barplot(df['Category'],df['Profit'],y = y)


# In[41]:


x ,y = plt.subplots(figsize=(10,6))
se.barplot(df['Category'],df['Discount'],y = y)


# In[42]:


p = df.groupby(['Sub-Category'])[['Profit','Discount','Sales']].mean()
p = p.sort_values('Profit')
p[['Profit']].plot(kind="bar",figsize=(10,8))
plt.ylabel("Profit")
plt.show()


# In[43]:


p = df.groupby(['Sub-Category'])[['Profit','Discount','Sales']].mean()
p = p.sort_values('Sales')
p[['Sales']].plot(kind="bar",figsize=(10,8))
plt.ylabel("Sales")
plt.show()


# In[44]:


p = df.groupby(['Sub-Category'])[['Profit','Discount','Sales']].mean()
p = p.sort_values('Discount')
p[['Discount']].plot(kind="bar",figsize=(10,8))
plt.ylabel("Discount")
plt.show()


# In[45]:


p = df.groupby(['State'])[['Profit','Discount','Sales']].mean()
p = p.sort_values('Profit')
p[['Profit']].plot(kind="bar",figsize=(10,8),color = "violet")
plt.ylabel("Profit")
plt.show()


# In[46]:


p = df.groupby(['State'])[['Profit','Discount','Sales']].mean()
p = p.sort_values('Discount')
p[['Discount']].plot(kind="bar",figsize=(10,8),color = 'green')
plt.ylabel("Discount")
plt.show()


# In[47]:


p = df.groupby(['State'])[['Profit','Discount','Sales']].mean()
p = p.sort_values('Sales')
p[['Sales']].plot(kind="bar",figsize=(10,8),color = 'yellow')
plt.ylabel("Sales")
plt.show()


# In[48]:


x,y = plt.subplots(nrows = 2, ncols = 2, figsize = (10,10))
se.distplot(df['Profit'],ax = y[0][0],color = "orange")
se.distplot(df['Discount'],ax = y[0][1],color = "purple")
se.distplot(df['Sales'],ax = y[1][0],color = "green")
se.distplot(df['Quantity'],ax = y[1][1],color = "pink")
y[0][0].set_title("Profit",fontsize = 20)
y[0][1].set_title("Discount",fontsize = 20)
y[1][0].set_title("Sales",fontsize = 20)
y[1][1].set_title("Quantity",fontsize = 20)
plt.tight_layout


# # Thank you!!!!
