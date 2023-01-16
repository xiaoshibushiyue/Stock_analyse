from Stock_helper.stock_now import stock_now_p
import pandas as pd

# List of Tuples
fruit_list = [ ('Orange', 34, 'Yes' )]
#Create a DataFrame object
df = pd.DataFrame(fruit_list, columns = ['Name' , 'Price', 'Stock'])
#Add new ROW
df.loc[1]=[ 'Mango', 4, 'No' ]
df.loc[2]=[ 'Apple', 14, 'Yes' ]
df.loc[len(df.index)] =[ 'Apple1', 13, 'Yes' ]
print(df)
stock_now_p('601012')