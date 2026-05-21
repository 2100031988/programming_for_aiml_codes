# PANDAS

# it is widely used for working with data

# We can do the following with pandas : 
# -- import spreadsheets
# -- analyze data
# -- clean and manipulate data
# -- prep data for visualization or machine learning

# pandas are imported as " import pandas " and nicknamed as pd

# Dataframe 
# is 2d datastructure made up of rows and columns and we can think of it as a sql table or a 
# excel spreadsheet data. We can easily sort, filter, group, modify, and analyze data using dataframe

import pandas as pd

# Method 1

data = {
    'City' : ['Delhi', 'Melbourne', 'Chicago', 'Madrid'],
    'Country' : ['India', 'Australia', 'USA', 'Spain'],
    'Population' : [100000, 200000, 500000, 700000]
}

df = pd.DataFrame(data)
print(df)

#  <----------------------------------------------------->

# Method 2 : creating from a list of list

data = [
    ['Delhi', 'India', 100000],
    ['Melbourne', 'Australia', 200000],
    ['Chicago', 'USA',  ],
    ['Madrid', 'Spain', 700000]
]

df = pd.DataFrame(data, columns=['city', 'country', 'population'])
print(df)

#  <----------------------------------------------------->

# To read a csv file in pandas
df = pd.read_csv('data.csv')

#  <----------------------------------------------------->

# View rows with .head() and .tail()

df.head()       # view first 5 rows
print("/n")

df.tail()       # view last 5 rows
print(df)

# -- if we want more than 5 rows then just pass the number inside the argument
# -- df.head(10)
# -- df.tail(10)

#  <----------------------------------------------------->

# .info() method shows us information about each column in our dataset
# we see Nan values (Not a number) often and it is because of missing or misleading values in our dataset

df.info()
print(df)

# Let's take an example of movies datset and here is the information using .info()

# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 5 entries, 0 to 4
# Data columns (total 8 columns):
#  #   Column           Non-Null Count  Dtype
# ---  ------           --------------  -----
#  0   title            5 non-null      object
#  1   release_date     5 non-null      object
#  2   genre            5 non-null      object
#  3   studio           5 non-null      object
#  4   budget           4 non-null      float64
#  5   box_office       4 non-null      float64
#  6   runtime_minutes  5 non-null      int64
#  7   rating           5 non-null      float64
# dtypes: float64(3), int64(1), object(4)
# memory usage: 312.0+ bytes

# We can see that:
# 1. 5 entries means that there are 5 rows in the dataset.
# 2. The budget and box_office columns are each missing 1 value (only 4 non-null).
# 4. 3. The Dtype data describes the data type of each column.

# 5. Decimal numbers are stored as float64 and whole numbers are stored as int64.
# 6. Columns that store strings are represented by object. If the columns store other complex data types, 
#    like dictionaries, dates, or user-defined objects, they would also appear as object.

#  <----------------------------------------------------->

# Summary Statistics with .describe()

# it gives us the summary statistics for every numeric column like 
# (mean, median, mode, standard deviation, etc)

df. describe() 

# if we want to view stats about non-numeric columnns like string we use include='all'

df.describe(include='all')

