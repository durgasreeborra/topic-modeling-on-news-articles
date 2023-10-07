#!/usr/bin/env python
# coding: utf-8

# In[4]:


import os
import pandas as pd

# Create an empty dictionary to store data categorized by different categories.
data = {}
categories = ["business", "entertainment", "politics", "sport", "tech"]

# Define a dictionary to store exploration results.
exploration_results = {}

# Loop through each category.
for category in categories:
    category_data = []
    category_dir = os.path.join("D:\data\Temp", category)
    
    file_list = os.listdir(category_dir)
    for file_name in file_list:
        with open(os.path.join(category_dir, file_name), 'r', encoding='iso-8859-1') as file:
            text = file.read()
            # Remove spaces between words
            text = ' '.join(text.split())  # This removes extra spaces
            category_data.append(text)
    
    # Store the category's data in the 'data' dictionary.
    data[category] = category_data
    
    # Perform data exploration for the current category.
    num_documents = len(category_data)
    total_characters = sum(len(doc) for doc in category_data)
    average_characters = total_characters / num_documents
    
    # Store exploration results in the 'exploration_results' dictionary.
    exploration_results[category] = {
        "Num Documents": num_documents,
        "Total Characters": total_characters,
        "Average Characters per Document": average_characters,
    }

# Task 2.1.1: Display the dataset's structure (first few rows)
print("Task 2.1.1: Display the dataset's structure (first few rows)")
for category, category_data in data.items():
    print(f"Category: {category}")
    for i, document in enumerate(category_data[:5]):
        print(f"Document {i + 1}: {document[:100]}...")  # Display the first 100 characters

# Task 2.1.2: Print column names and data types
print("\nTask 2.1.2: Print column names and data types")
for category, category_data in data.items():
    print(f"Category: {category}")
    df = pd.DataFrame({'Text': category_data})
    print(df.dtypes)
    print()

# Check for Missing Values:

# Task 2.1.3: Identify missing values and provide a summary
print("Task 2.1.3: Identify missing values and provide a summary")
for category, category_data in data.items():
    print(f"Category: {category}")
    df = pd.DataFrame({'Text': category_data})
    missing_values = df.isnull().sum()
    print(missing_values)
    print()

# Summary Statistics: (Not applicable to text data)

# Task 2.1.4: Compute summary statistics for text lengths
print("Task 2.1.4: Summary Statistics for Text Lengths")
for category, category_data in data.items():
    print(f"Category: {category}")
    df = pd.DataFrame({'Text': category_data})
    df['Text Length'] = df['Text'].apply(len)
    summary_stats = df['Text Length'].describe(percentiles=[.25, .75])
    print(summary_stats[['count', 'mean', 'std', 'min', 'max']])
    print()




# In[ ]:




