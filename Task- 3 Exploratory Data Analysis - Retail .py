#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = "SampleSuperstore.csv"
data = pd.read_csv(file_path)

# Display the first few rows of the dataset
data.head()

# Check for missing values
data.isnull().sum()

# Summary statistics
data.describe()

# Analyze Categories
plt.figure(figsize=(10, 6))
sns.countplot(x='Category', data=data)
plt.title('Distribution of Categories')
plt.show()



# Identify Weak Areas
# Look for categories or sub-categories with low profit margins.
# Identify regions or states where sales are low or where returns are high.
# Analyze customer segments with low purchasing power.

# Make Recommendations
# Focus on improving the profitability of specific categories or sub-categories.
# Implement strategies to reduce returns in problematic regions.
# Target marketing efforts towards customer segments with higher potential.


# In[2]:


# Analyze Sub-Categories
plt.figure(figsize=(12, 6))
sns.countplot(x='Sub-Category', data=data, order=data['Sub-Category'].value_counts().index)
plt.title('Distribution of Sub-Categories')
plt.xticks(rotation=45)
plt.show()


# In[3]:


# Analyze Profit by Category
plt.figure(figsize=(12, 6))
sns.boxplot(x='Category', y='Profit', data=data)
plt.title('Profit Distribution by Category')
plt.show()


# In[4]:


# Analyze Profit by Sub-Category
plt.figure(figsize=(14, 6))
sns.boxplot(x='Sub-Category', y='Profit', data=data, order=data.groupby('Sub-Category')['Profit'].median().sort_values().index)
plt.title('Profit Distribution by Sub-Category')
plt.xticks(rotation=45)
plt.show()


# In[6]:


# Visualize sales by category
plt.figure(figsize=(10, 6))
sns.barplot(x='Category', y='Sales', data=data, ci=None)
plt.title('Sales by Category')
plt.show()


# In[7]:


# Visualize profit by sub-category
plt.figure(figsize=(14, 8))
sns.barplot(x='Sub-Category', y='Profit', data=data, ci=None)
plt.title('Profit by Sub-Category')
plt.xticks(rotation=45, ha='right')
plt.show()


# In[8]:


# Visualize sales and profit by region
plt.figure(figsize=(12, 6))
sns.barplot(x='Region', y='Sales', data=data, ci=None, color='skyblue', label='Sales')
sns.barplot(x='Region', y='Profit', data=data, ci=None, color='orange', label='Profit')
plt.title('Sales and Profit by Region')
plt.legend()
plt.show()


# In[9]:


# Correlation heatmap
correlation_matrix = data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()


# In[12]:


# Top 10 products by sales
top_products = data.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False).head(10)
plt.figure(figsize=(12, 6))
top_products.plot(kind='bar', color='purple')
plt.title('Top 10 Products by Sales')
plt.xlabel('Sub-Category')
plt.ylabel('Total Sales')
plt.show()


# ## Key Findings:
# 
# Binders, Paper, Furnishings, Phones, and Chairs were the top-selling sub-categories.
# Tables, Bookcases, Supplies, and Copiers had low profit margins.
# Central and South regions had high sales, but West and East offered potential for improvement.
# Positive correlation between sales and quantity, negative correlation between discounts and profit.

# In[ ]:




