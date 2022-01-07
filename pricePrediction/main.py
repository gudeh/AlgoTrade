import pygsheets
import pandas as pd
import LSTM
#authorization
gc = pygsheets.authorize(service_file='#REMOVED FOR PRIVACY')

# Create empty dataframe
df = pd.DataFrame()

# Create a column
#df['name'] = ['John', 'Steve', 'Sarah']
df=LSTM.myCall()

#open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
sheet = gc.open('LSTM')

#select the first sheet 
#wks = sheet[0]
cells = sheet[0].get_all_values(include_tailing_empty_rows=False, include_tailing_empty=False, returnas='matrix')
last_row = len(cells)
new_row=list(df.iloc[0])
print(new_row)
sheet[0].insert_rows(last_row, number=1, values= new_row)

cells = sheet[1].get_all_values(include_tailing_empty_rows=False, include_tailing_empty=False, returnas='matrix')
last_row = len(cells)
print("->",df.iloc[1])
new_row=list(df.iloc[1])
print(new_row)
sheet[1].insert_rows(last_row, number=1, values= new_row)
