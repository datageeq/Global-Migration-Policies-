#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt


# In[3]:


file_path = r"C:\Users\Sietoyo\Downloads\facilitate-orderly-safe-migration.csv"
df = pd.read_csv(file_path)


# In[5]:


# Step 2: Calculate Changes
# Pivot the data to have years as columns
df_pivot = df.pivot(index='Entity', columns='Year', values='10.7.2 - Countries with migration policies to facilitate orderly, safe, regular and responsible migration and mobility of people, by policy domain (1 = Requires further progress; 2 = Partially meets; 3 = Meets; 4 = Fully meets) - SG_CPA_MIGRS - All Domains').reset_index()


# In[6]:


# Calculate the change in scores from 2019 to 2021
df_pivot['Change'] = df_pivot[2021] - df_pivot[2019]


# In[7]:


# Step 3: Classify Changes
def classify_change(change):
    if change > 0:
        return 'Progress'
    elif change < 0:
        return 'Regression'
    else:
        return 'No Change'
df_pivot['Classification'] = df_pivot['Change'].apply(classify_change)


# In[8]:


# Step 4: Descriptive Statistics
summary = df_pivot['Classification'].value_counts().reset_index()
summary.columns = ['Classification', 'Count']


# In[9]:


# Step 5: Visualization
# Bar Chart
plt.figure(figsize=(8, 6))
plt.bar(summary['Classification'], summary['Count'], color=['green', 'red', 'grey'])
plt.title('Progress Identification in Migration Policies (2019 to 2021)')
plt.xlabel('Classification')
plt.ylabel('Number of Countries')
plt.show()


# In[10]:


# Detailed Table
detailed_table = df_pivot[['Entity', 2019, 2021, 'Change', 'Classification']]
print(detailed_table)


# In[11]:


# Summary
print(summary)


# In[14]:


# Detailed Tables for Progress and Regression
print("Countries that made progress:")
print(progress_countries)


# In[15]:


print("\nCountries that regressed:")
print(regression_countries)


# In[16]:


# Summary
print(summary)

