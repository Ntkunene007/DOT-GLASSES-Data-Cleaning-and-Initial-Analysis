#!/usr/bin/env python
# coding: utf-8

# ## 1. Data Cleaning

# In[1]:


import pandas as pd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


# Loading the dataset
spectacles_data = pd.read_csv('Dots Potential Customer Survey Data - Sheet1.csv')


# In[3]:


spectacles_data.head()


# In[4]:


# Displaying basic information about the dataset

print(spectacles_data.info())


# In[5]:


spectacles_data.describe()


# In[6]:


spectacles_data.columns


# In[7]:


spectacles_data.isnull().sum()


# In[8]:


# Handling missing values

spectacles_data.dropna(inplace=True)


# In[9]:


# Removing duplicate rows if any

spectacles_data.drop_duplicates(inplace=True)


# ## 2. Exploratory Data Analysis (EDA)

# In[10]:


# Exploring the distribution of age

plt.figure(figsize=(10, 6))
sns.histplot(spectacles_data['Age'], bins=20, kde=True)
plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()


# In[11]:


# Exploring the correlation between variables

plt.figure(figsize=(12, 8))
sns.heatmap(spectacles_data.corr(), annot=True, cmap='coolwarm', linewidths=.5)
plt.title('Correlation Matrix')
plt.show()


# In[12]:


# Exploring categorical variables

sns.countplot(x='Gender', data=spectacles_data)
plt.title('Distribution of Gender')
plt.show()


# ## 3. Plotting Data for Insights

# In[13]:


# Exploring the distribution of health scores for people wearing glasses and not wearing glasses

plt.figure(figsize=(10, 6))
sns.boxplot(x='Wear Specs', y='IQ', data=spectacles_data)
plt.title('IQ Distribution for People Wearing and Not Wearing Glasses')
plt.xlabel('Wear Specs')
plt.ylabel('IQ')
plt.show()


# In[14]:


# Exploring the distribution of health scores for people wearing glasses and not wearing glasses

plt.figure(figsize=(10, 6))
sns.boxplot(x='Wear Specs', y='IQ', data=spectacles_data)
plt.title('IQ Distribution for People Wearing and Not Wearing Glasses')
plt.xlabel('Wear Specs')
plt.ylabel('IQ')
plt.show()


# In[15]:


# Calculating the correlation matrix

correlation_matrix = spectacles_data.corr()
correlation_matrix


# In[16]:


# Creating the heatmap

sns.heatmap(correlation_matrix)


# In[17]:


# Counting the occurrences of each Uniuque ID

track_counts = spectacles_data['Unique ID'].value_counts()
track_counts


# In[ ]:





# In[18]:


# Exploring relationships between variables

sns.scatterplot(x='Age', y='IQ', hue='Wear Specs', data=spectacles_data)
plt.title('Age vs IQ')
plt.xlabel('Age')
plt.ylabel('IQ')
plt.show()


# In[19]:


# Selecting the columns to be plotted

columns = ['Time spent watching videos/TV', 'Time spent playing indoor sports', 'Time spent playing outdoor sports', 'Total Time spent working in front of screen', 'Sleeping hours',
    'Whether parents have specs', 'Migrated within country', 'Migrated overseas', 'Maritial Status (0 - Single, 1 - Married, 2 - Divorced)','Has Gym Subscription']

# Setting up the subplots using Seaborn's 'subplot' function
plt.figure(figsize=(10, 18))
plt.subplots_adjust(hspace=0.5)

for i, col in enumerate(columns, 1):
    plt.subplot(5, 2, i)
    sns.histplot(spectacles_data[col])
    plt.title(col.capitalize())

plt.show()


# In[ ]:




