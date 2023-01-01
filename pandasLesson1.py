# -*- coding: utf-8 -*-
"""
Created on Sat Dec 31 16:56:24 2022

@author: sam.woodbeck
"""

##Following a tutorial about pandas dataframes from: https://pandas.pydata.org/docs/getting_started/intro_tutorials/01_table_oriented.html

#%%  Import Cell
import pandas as pd #importing pandas for data structures

#%% DataFrames
# I want to store data on my teammates.  I know their name, age, and sex.
df = pd.DataFrame(
    {
        "Name": [ #Creating a column with the header "Name".  Also can be thought of a creating a series "Name" with three textual items.
                 "Jake the Dog", #Creating a row
                 "Finn the Human",
                 "Ice King"
        ],
        "Age": [12, 28, 1043],
        "Sex": ["Male", "Male", "Male"]
    }
)
df  #displays the dataframe we just built

#%%  Ages
# Each Column in a DataFrame is a Series
# I'm just interested in the ages.
df["Age"] #just returns the column "Age" from the dataframe we created above.
          #The result is a series.
          
ages = pd.Series([12, 28, 1043], name="Age")    #Explicitly creating a series from scratch
ages

#Do Something with a DataFrame or Series
#I want to know the maximum age of my teammates.
#%%
df["Age"].max()  #Selects the column "Age" from the DataFrame df, then applies the max() method/function to return the maximum value in that column.
#%%
ages.max()  #applies the max() method/function to the series "ages"
#%%
df.describe()  #Returns a table/DataFrame with some simple statistics about the numberical columns in the DataFrame df
