import os
import csv
import pandas as pd
file = os.path.join("Resources", "budget_data.csv")
file_df= pd.read_csv(file)
file_df.head(5)
monthcount = file_df.iloc[:,0]
profitloss=file_df.loc[:,"Profit/Losses"]
avg = sum(profitloss)/len(profitloss)
print(f"Total Months: {monthcount.count()}")
print(f"Total: $ {sum(profitloss)}")
print(f"Average Change: $ {round(avg)}")
print(f"Greatest Increase in Profits: ${max(profitloss)}")
print(f"Greatest Decrease in Profits: ${min(profitloss)}")
output_path = os.path.join("Analysis","Results.txt")
with open(output_path, 'w') as text_file:
    text_file.write(f"Total Months: {monthcount.count()}\n")
    text_file.write(f"Total: $ {sum(profitloss)}\n")
    text_file.write(f"Average Change: $ {round(avg)}\n")
    text_file.write(f"Greatest Increase in Profits: ${max(profitloss)}\n")
    text_file.write(f"Greatest Decrease in Profits: ${min(profitloss)}\n")