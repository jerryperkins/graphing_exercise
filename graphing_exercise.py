import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel('data/Share of US Ad Spend.xlsx')

print(df)
print(df.info()) # no nans

df = df.drop([1,2,10,11]) #dropping subcategories as I don't want that much breakdown in this situation
df = df.drop(columns=[2021, 2022, 2023, 2024, 'Type']) # I only want past data and not projections

columns_temp = df.drop(columns=['Source'])
columns_temp = columns_temp.div(1000000) #makes the numbers easier to read and I don't have to deal with exponents
list_columns = columns_temp.columns.values # getting the years into a list

plt.rcParams['figure.figsize'] = 12,6
def plot_each_source():
    rows = [0,3,4,5,6,7,8,9] #probably a better way to get this list of indices ;)
    for x in rows:
        row_data = columns_temp.loc[x].values # getting values of each row
        labels = df['Source'][x] # getting the names of each row
        plt.plot( list_columns, row_data, label = labels)
plot_each_source()    
plt.legend(loc =(1.02,0))    
plt.ylabel('Dollars Spent in Millions')
plt.xlabel('Year')
plt.title("Advertising $$$ Through the Years")
plt.ylim(top=125000, bottom = 0)
plt.xlim(left = 2012, right = 2020)
plt.tight_layout()

plt.show()