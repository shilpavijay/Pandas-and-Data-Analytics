import pandas as pd

df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2001, 2002, 2003, 2004])

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2, 3, 2, 2],
                    'US_GDP_Thousands':[50, 55, 65, 55]},
                   index = [2005, 2006, 2007, 2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Unemployment':[7, 8, 9, 6],
                    'Low_tier_HPI':[50, 52, 50, 53]},
                   index = [2001, 2002, 2003, 2004])

########Concatenating datasets##########
#####

concat = pd.concat([df1,df2,df3])
print (concat)

########Appending ###########################


df4 = df1.append(df2)
print (df4)


##########Merging  datasets#############

df4 = pd.merge(df1,df2, on = ['HPI'])
df4.set_index('HPI',inplace=True)
print(df4)

# ###########Joining Datasets############

df1.set_index('HPI', inplace=True)
df3.set_index('HPI', inplace=True)

joined = df2.join(df3)
print(joined)
