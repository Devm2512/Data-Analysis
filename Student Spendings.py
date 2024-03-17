#!/usr/bin/env python
# coding: utf-8

# In[1]:


# https://www.kaggle.com/datasets/sumanthnimmagadda/student-spending-dataset
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df = pd.read_csv('C:/Users/DEV/Downloads/student_spendings.csv')


# In[3]:


df


# In[4]:


df.drop(columns = ['Unnamed: 0'],axis =1,inplace = True)


# In[5]:


df


# In[6]:


df.info()


# Observations from the info functions.
# 1) No missing values in the data
# 2) Correct datatype for each  column

# In[7]:


# Let us analyze all the columns one by one.
# Let us start with age
# Unique values in age
sorted(df['age'].unique().tolist())


# There are 8 unique values in age from 18 to 25

# In[8]:


# let us count the value for age
pd.DataFrame(df['age'].value_counts().sort_index())


# In[9]:


# let us find the unique values in gender
df['gender'].unique()


# There are 3 different values in gender

# In[10]:


pd.DataFrame(df['gender'].value_counts())


# In[11]:


# Let us find the year in school
df['year_in_school'].unique()


# There are 4 unique values in year in school

# In[12]:


pd.DataFrame(df['year_in_school'].value_counts().sort_index())


# In[13]:


# Let find the unique values in major
df['major'].unique()


# There are 5 unique values in major

# In[14]:


pd.DataFrame(df['major'].value_counts())


# In[15]:


# Now let us analyze the columns age, year, major, and gender with other columns bivariate analysis


# In[16]:


total_income_by_age = df.groupby('age')['monthly_income','financial_aid'].sum()


# In[17]:


total_income_by_age['total'] = total_income_by_age['monthly_income'] + total_income_by_age['financial_aid']


# In[18]:


total_income_by_age['avg_income'] = total_income_by_age['total']/df['age'].value_counts().sort_index()


# In[19]:


total_income_by_age.sort_values('avg_income',ascending = False)


# Even though the highest amount is alloted to student with age 25 years old. the highest average income of student is of 19 years old
# Even though the total least amount is allowted to 20 years old the average least amount spent on student is 1479 which is on 22 year old students

# In[20]:


total_spending_by_age = df.groupby('age')['tuition','housing','food','transportation','books_supplies','entertainment','personal_care','technology','health_wellness','miscellaneous'].sum()


# In[23]:


total_spending_by_age['Total'] = total_spending_by_age['tuition']+ total_spending_by_age['housing']+ total_spending_by_age['food']+ total_spending_by_age['transportation']+ total_spending_by_age['books_supplies']+ total_spending_by_age['entertainment']+ total_spending_by_age['personal_care']+total_spending_by_age['technology']+ total_spending_by_age['health_wellness']+total_spending_by_age['miscellaneous']


# In[24]:


total_spending_by_age


# In[25]:


for i in range(len(total_spending_by_age.columns)):
    print(total_spending_by_age.columns[i])
    print(total_spending_by_age.sort_values(total_spending_by_age.columns[i],ascending = False))


# Information On Spending
# 1) Tution
#     Max : Age 25
#     Min : Age 19
# 2) Housing
#     Max : Age 25
#     Min : Age 19
# 3) Food
#     Max : Age 25
#     Min : Age 19
# 4) Transpotation
#     Max : Age 25
#     Min : Age 20
# 5) Book and Supplies
#     Max : Age 25
#     Min : Age 19
# 6) Entertainment
#     Max : Age 25
#     Min : Age 19
# 7) Personal Care 
#     Max : Age 24
#     Min : Age 20
# 8) Technology
#     Max : Age 25
#     Min : Age 20
# 9) Health and Wellness
#     Max : Age 25
#     Min : Age 19
# 10) Miscellaneous
#     Max : Age 25
#     Min : Age 20
# 11) Total
#     Max : Age 25
#     Min : Age 19

# In[ ]:





# In[ ]:




