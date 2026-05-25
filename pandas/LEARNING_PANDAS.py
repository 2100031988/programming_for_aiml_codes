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



employee = {
    'name' : ['sabya', 'vincent', 'sam', 'jeffery', 'ethan'],
    'id' : [1, 2, 3, 4, 5],
    'position' : ['ceo', 'ai engineer', 'developer', 'marketing manager', 'cmo'],
    'experience' : [10, 8, 3, 7, 9],
    'salary' : [25000, 1300, 2000, 15000, 220000]
}

df = pd.DataFrame(employee)
print(df)

dff = pd.read_csv('data.csv')
dff.head()
dff.tail()
dff.info()
dff.describe()
dff.describe(include='all')

#  <----------------------------------------------------->

# Accessing Specific Columns
# suppose we want to extract only the specific column then we can do it as:

# (df['column_name']) 
# movies.genre / movies['genre'] 

#  <----------------------------------------------------->

# Series
# It is like a single column of the table [here, the table is like a dataframe as an example]

# type(movies)              # returns pandas.core.frame.DataFrame
# type(movies['genre'])

#  <----------------------------------------------------->

# Accessing Multiple Columns
# we can access multiple columns using python's list of column names

# genre_and_studio_df = movies[['genre', 'studio']]

# basic_stats = characters[['name', 'level', 'hp']] # if there is 2,3,4,5,6 any number but bracket only 2
# print(basic_stats)

# it returns multiple columns

#  <----------------------------------------------------->

# Accessing All But One Column with .drop()
# it is used when we want to drop everything except one column

# remove_title_df = movies.drop("title", axis=1)
# it tells pandas that we want to drop title column only.


#  <----------------------------------------------------->


# Filtering Rows
# to filter only rows we can do like this:

# long_movies = movies[movies[runtime_movies] > 120]

# we need to understand that why we kept two movies in outside bracket and this comes to
# our understanding that first it turns those values into true or false like which movie length is
# larger than 120 minutes and then the outer movies will filter those values and print those which are >120.

#  <----------------------------------------------------->

#  AND and OR
# You can filter based on multiple conditions by using AND (&) and OR (|).
# For example, if you wanted to filter for movies that are longer than 120 minutes 
# AND in the genre 'Sci-Fi'

# long_movies = movies[
#   (movies['runtime_minutes'] > 120) &
#   (movies['genre'] == 'Sci-Fi')               # the and operator can be used to check two operations 
# ]                                             # it is important bro


#  <----------------------------------------------------->


# Sorting, Renaming, and Adding Columns

# Sorting By Columns with .sort_values()
# we can sort the values by using .sortvalues method and by a specific column as well.

# box_sorted_values = movies.sort_values(by = 'box_office' , ascending = False)     # descinding order

# box_sorted_values = movies.sort_values(by = 'box_office' , ascending = True)      # ascending order

#  <----------------------------------------------------->

# Rename Columns with .rename()
# we can change the row name using .rename()

# movies = movies.rename(columns={'budget' : 'budget_usd'})     # here changing budget to budget_usd

# this does not change in the memory meaning not in the table that we are working or datset bro
# if we want to chnage then we should use inplace = 'true'

# movies = movies.rename(columns={'budget' : 'budget_usd'}, inplace = True) 

#  <----------------------------------------------------->

# Adding Columns
# we can add new columns by assigning a list or a collection to a column name

# movies['lead_actor'] = ['Keanu Reeves', 'Leonardo DiCaprio', 'Song Kang-ho', 'Matthew Broderick', 'Michelle Yeoh']

# alternatively we can also do it like this way to add budget in millions okk

# movies['budget (millions)'] = movies['budget'] / 1000000



