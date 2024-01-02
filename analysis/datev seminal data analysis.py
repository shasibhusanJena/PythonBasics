#!/usr/bin/env python
# coding: utf-8

# In[34]:


import pandas as pd


# In[36]:


data_frame = pd.read_csv('C:/Users/shjena/Downloads/2023-10-30-cdp_person_seminar.csv', sep='\t')


# In[37]:


#displaying first five rows
display(data_frame.head())

#displaying last five rows
display(data_frame.tail())


# In[38]:


data_frame.info()


# In[39]:


data_frame.isnull().sum()


# In[40]:


# count all values in name column in ascending order
print(data_frame['Langbezeichnung externes Produkt'].value_counts(ascending=True))


# In[43]:


# Replace 'column_name' with the name of your specific column
column_to_search = 'Langbezeichnung externes Produkt'

# Count occurrences of 'abc' in the specified column
abc_count = (data_frame[column_to_search] == 'Qualifizierungsangebote').sum()

print(f"The count of 'abc' in '{column_to_search}' column is: {abc_count}")


# In[ ]:




