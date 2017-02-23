import pandas as pd

df = pd.read_csv('housing.csv')

# print(df.head())

# df.set_index('Date',inplace=True)
# df.to_csv('newtest.csv')

######## explicitly specify not to have an index col #########

df2 = pd.read_csv('newtest.csv',index_col = 0)
print(df2.head())

######### Rename columns ##########

# df2.columns = ['A','B','C']
# print(df2.head())

########## Rename a single column ##########

df2.rename(columns={'Home Price Index':'HPI'},inplace=True)
print(df2.head())


####### Choose not to save the header #####

# df2.to_csv('newtest1.csv',header=False)

####### read a csv without headers and manually assign headers to them #####

# df3 = pd.read_csv('newtest1.csv', names=['HPI','RI','HWE'], index_col=0)
# print(df3.head())

##### Convert to other formats #######

# df3.to_html('test.html')