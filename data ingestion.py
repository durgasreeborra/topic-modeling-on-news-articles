#!/usr/bin/env python
# coding: utf-8

# In[9]:


import os
data = {}
categories = ["business", "entertainment", "politics", "sport", "tech"]

for category in categories:
    category_data = []
    category_dir = os.path.join("D:\data\Temp", category)
    
    file_list = os.listdir(category_dir)
    for file_name in file_list:
        with open(os.path.join(category_dir, file_name), 'r', encoding='iso-8859-1') as file:
            text = file.read()
            category_data.append(text)
    data[category] = category_data
data


# In[ ]:




