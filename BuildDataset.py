import quandl
import pandas as pd

api_key = open('quandlapikey.txt','r').read()

# df = quandl.get("FMAC/HPI_AZ", authtoken=api_key)
# print(df.head())

states_list = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
# print(states_list[0][0])

for abbv in states_list[0][0][1:]:
	# print("FMAC/HPI_" + str(abbv))
	df = quandl.get("FMAC/HPI_" + str(abbv),authtoken=api_key)
	# print(df.head())

