import quandl
import pandas as pd
import pickle
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

api_key = open('quandlapikey.txt','r').read()

# df = quandl.get("FMAC/HPI_AZ", authtoken=api_key)
# print(df.head())



def state_names():
	states_list = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
	return states_list[0][0][1:]


def get_all_data():
	main_df = pd.DataFrame()
	states = state_names()
	for abbv in states:
		query = "FMAC/HPI_" + str(abbv)
		df = quandl.get(query,authtoken=api_key)
		df.rename(columns={'Value':abbv},inplace=True)
		# print(df.head())

		if main_df.empty:
			main_df = df
		else:
			main_df = main_df.join(df)

	pickle_out = open('states_HPI.pickle','wb')
	pickle.dump(main_df,pickle_out)
	pickle_out.close()

# get_all_data()

# pickle_in = open('states_HPI.pickle','rb')
# HPI = pickle.load(pickle_in)
# print(HPI)

########## Pandas has its own pickle:

# HPI_data.to_pickle('pickle.pickle')
# HPI_data2 = pd.read_pickle('pickle.pickle')
# print(HPI_data2)

HPI_data = pd.read_pickle('states_HPI.pickle')

########## Changing column data ###############

# HPI_data['AZ2'] = HPI_data['AZ'] * 2
# print(HPI_data[['AZ','AZ2']])

########## plotting data using Matplotlib ####

HPI_data.plot()
plt.legend().remove()
plt.show()

