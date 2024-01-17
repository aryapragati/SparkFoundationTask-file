#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd

# Specify the file path and encoding
file_path = r'C:\Users\aryap\Spark Foundation Task- 1\global_terroris.csv'
encoding_type = 'ISO-8859-1'  # You may also try 'latin1' or other encodings

# Read the CSV file into a DataFrame
df = pd.read_csv(file_path, encoding=encoding_type)

# Display the DataFrame (optional)
print(df)


# In[15]:


# Drop rows with missing values
df_cleaned = df.dropna()

# Alternatively, fill missing values with mean or other strategies
# df_cleaned = df.fillna(df.mean())


# In[16]:


df_cleaned = df.drop_duplicates()


# In[17]:


# Example: Keep only a subset of columns
selected_columns = ['eventid', 'iyear', 'imonth', 'iday', 'country', 'country_txt', 'region', 'city', 'attacktype1_txt', 'nkill', 'nwound']
df_cleaned = df[selected_columns]


# In[23]:


# Example: Convert 'nkill' and 'nwound' to numeric using .loc
df_cleaned = df.copy()
df_cleaned['nkill'] = pd.to_numeric(df_cleaned['nkill'], errors='coerce')
df_cleaned['nwound'] = pd.to_numeric(df_cleaned['nwound'], errors='coerce')


# In[33]:


# Rename columns
df_cleaned.rename(columns={'iyear': 'year', 'imonth': 'month', 'iday': 'day'}, inplace=True)


# In[35]:


# Convert 'year', 'month', and 'day' to datetime
df_cleaned['date'] = pd.to_datetime(df_cleaned[['year', 'month', 'day']], errors='coerce')


# In[ ]:


# Example: Drop columns not needed
#df_cleaned = df_cleaned.drop(['imonth', 'iday'], axis=1)


# In[43]:


pip install geopandas


# In[45]:


import matplotlib.pyplot as plt
import geopandas as gpd

# Plotting the geographical distribution
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
df_geo = df_cleaned.groupby('country_txt').size().reset_index(name='incident_count')
world = world.merge(df_geo, how='left', left_on='name', right_on='country_txt')
world.plot(column='incident_count', cmap='OrRd', figsize=(15, 10), legend=True)
plt.title('Global Terrorism - Geographical Distribution')
plt.show()


# Plot the geographical distribution of terrorist incidents using maps or scatter plots.
# Identify countries and regions with the highest number of incidents.

# # 3. Temporal Analysis:
# Analyze the number of incidents over time to identify trends.
# Explore patterns by year, month, and day.

# In[47]:


# Rename columns
df_cleaned.rename(columns={'iyear': 'year', 'imonth': 'month', 'iday': 'day'}, inplace=True)

# Analyzing incidents over time
df_cleaned['year_month'] = df_cleaned['date'].dt.to_period('M')
incidents_by_year = df_cleaned['year'].value_counts().sort_index()

# Plotting incidents over time
plt.figure(figsize=(15, 6))
incidents_by_year.plot(kind='line')
plt.title('Global Terrorism - Incidents Over Time')
plt.xlabel('Year')
plt.ylabel('Number of Incidents')
plt.grid(True)
plt.show()


# # 4. Attack Type Analysis:
# Identify the most common types of terrorist attacks.

# In[48]:


# Analyzing the most common types of attacks
attack_types = df_cleaned['attacktype1_txt'].value_counts()

# Plotting the distribution of attack types
plt.figure(figsize=(12, 8))
attack_types.plot(kind='bar', color='skyblue')
plt.title('Global Terrorism - Distribution of Attack Types')
plt.xlabel('Attack Type')
plt.ylabel('Number of Incidents')
plt.xticks(rotation=45, ha='right')
plt.show()


# # 5. Target Analysis:
# Explore the types of targets that terrorists commonly attack.

# In[49]:


# Analyzing the most common types of targets
target_types = df_cleaned['targtype1_txt'].value_counts()

# Plotting the distribution of target types
plt.figure(figsize=(12, 8))
target_types.plot(kind='bar', color='lightcoral')
plt.title('Global Terrorism - Distribution of Target Types')
plt.xlabel('Target Type')
plt.ylabel('Number of Incidents')
plt.xticks(rotation=45, ha='right')
plt.show()


# # 6. Hot Zones Analysis:
# Identify specific countries or regions with the highest number of incidents.

# In[50]:


# Identifying hot zones (countries with the highest number of incidents)
hot_zones = df_cleaned['country_txt'].value_counts().head(10)

# Plotting the hot zones
plt.figure(figsize=(12, 8))
hot_zones.plot(kind='bar', color='salmon')
plt.title('Global Terrorism - Hot Zones')
plt.xlabel('Country')
plt.ylabel('Number of Incidents')
plt.xticks(rotation=45, ha='right')
plt.show()


# # 7. Group/Perpetrator Analysis:
# Analyze the involvement of terrorist groups or perpetrators.
# python
# 

# In[51]:


# Analyzing the most active terrorist groups
terrorist_groups = df_cleaned['gname'].value_counts().head(10)

# Plotting the distribution of terrorist groups
plt.figure(figsize=(12, 8))
terrorist_groups.plot(kind='bar', color='darkcyan')
plt.title('Global Terrorism - Most Active Terrorist Groups')
plt.xlabel('Terrorist Group')
plt.ylabel('Number of Incidents')
plt.xticks(rotation=45, ha='right')
plt.show()


# # 8. Casualty Analysis:
# Explore the number of casualties (killed and wounded).

# In[52]:


# Analyzing casualties
df_cleaned['total_casualties'] = df_cleaned['nkill'] + df_cleaned['nwound']

# Plotting the distribution of casualties
plt.figure(figsize=(12, 8))
df_cleaned.groupby('country_txt')['total_casualties'].sum().sort_values(ascending=False).head(10).plot(kind='bar', color='indianred')
plt.title('Global Terrorism - Countries with Highest Casualties')
plt.xlabel('Country')
plt.ylabel('Total Casualties')
plt.xticks(rotation=45, ha='right')
plt.show()


# In[ ]:




