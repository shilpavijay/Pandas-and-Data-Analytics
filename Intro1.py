import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

stats = {'Day':[1,2,3,4,5,6],
             'Visitors':[43,34,65,56,29,76],
             'Bounce Rate':[65,67,78,65,45,52]}

######## Creating a Data Frame ##########

df = pd.DataFrame(stats)   

######## Printing the Data Frame ##########
# print(df)
# print(df.head())
# print(df.tail(2))


######## Setting a new Index to the Data Frame ##########

# print(df.set_index('Day'))
#df = df.set_index('Day')
# OR
# df.set_index('Day', inplace=True)
# print(df.head())

######## Referencing columns of the Data Frame ##########

# print(df['Bounce Rate'])
# print(df.Visitors)
# print(df[['Bounce Rate','Visitors']])

######## Convert to a list ###########

print(df.Visitors.tolist())
print(np.array(df[['Bounce Rate','Visitors']]))

###### Convert a list/array to a DF ######

df2 = pd.DataFrame(np.array(df[['Bounce Rate','Visitors']]))
print(df2)