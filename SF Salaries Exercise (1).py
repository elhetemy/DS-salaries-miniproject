#!/usr/bin/env python
# coding: utf-8

# # SF Salaries Exercise 
# 
# 

# ** Import pandas as pd.**

# In[38]:


import pandas as pd
import numpy as np


# ** Read Salaries.csv as a dataframe called sal.**

# In[3]:


df=pd.read_csv('Salaries.csv')


# ** Check the head of the DataFrame. **

# In[4]:


df.head()


# ** Use the .info() method to find out how many entries there are.**

# In[5]:


df.info()


# **What is the average BasePay ?**

# In[7]:


df['BasePay'].mean()


# ** What is the highest amount of OvertimePay in the dataset ? **

# In[8]:


df['OvertimePay'].max()


# ** What is the job title of  JOSEPH DRISCOLL ? Note: Use all caps, otherwise you may get an answer that doesn't match up (there is also a lowercase Joseph Driscoll). **

# In[18]:


df['JobTitle'][df['EmployeeName']=='JOSEPH DRISCOLL']


# ** How much does JOSEPH DRISCOLL make (including benefits)? **

# In[19]:


df['TotalPayBenefits'][df['EmployeeName']=='JOSEPH DRISCOLL']


# ** What is the name of highest paid person (including benefits)?**

# In[21]:


df['EmployeeName'][df['TotalPayBenefits']==df['TotalPayBenefits'].max()]


# ** What is the name of lowest paid person (including benefits)? Do you notice something strange about how much he or she is paid?**

# In[23]:


df['EmployeeName'][df['TotalPayBenefits']==df['TotalPayBenefits'].min()]


# In[24]:


df[df['TotalPayBenefits']==df['TotalPayBenefits'].min()]


# there is no money in (-) this value should be reviewed and entered correctly

# ** What was the average (mean) BasePay of all employees per year? (2011-2014) ? **

# In[34]:


print(df['BasePay'][df['Year']==2014].mean())
print(df['BasePay'][df['Year']==2013].mean())
print(df['BasePay'][df['Year']==2012].mean())
print(df['BasePay'][df['Year']==2011].mean())


# ** How many unique job titles are there? **

# In[44]:


df['JobTitle'].nunique()


# ** What are the top 5 most common jobs? **

# In[66]:


df['JobTitle'].value_counts().head(5)


# ** How many Job Titles were represented by only one person in 2013? (e.g. Job Titles with only one occurence in 2013?) **

# In[69]:


df['JobTitle'][df['Year']==2013].nunique()


# ** How many people have the word Chief in their job title? (This is pretty tricky) **

# In[73]:


df['JobTitle'].str.count('CHIEF')


# only one has the word chief in his job title

# ** Bonus: Is there a correlation between length of the Job Title string and Salary? **

# In[77]:


df['JopTitleLength']=df['JobTitle'].apply(len)
df['JopTitleLength']


# In[78]:


df['JopTitleLength'].corr(df['TotalPayBenefits'])


# # Great Job!
