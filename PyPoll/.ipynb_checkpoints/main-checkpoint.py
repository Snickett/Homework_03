import os
import csv
import pandas as pd
file = os.path.join("Resources", "election_data.csv")
file_df= pd.read_csv(file)
file_df.isnull().any()
votercount = len(file_df.iloc[:,1])
file_df["Candidate"].unique()
totals_df = file_df["Candidate"].value_counts().rename_axis("Candidate").reset_index(name="Totals")
percents = round((totals_df["Totals"]/votercount)*100)
totals_df["Percent (%)"] = percents
df2= totals_df[totals_df.loc[:,"Totals"] ==max(totals_df["Totals"])]
print("Election Results")
print("-------------------------")
print(f"Total Votes: {votercount}")
print("-------------------------")
for r in range(0,4):
    print(f"{totals_df.iloc[r,0]}: {totals_df.iloc[r,2]}% ({totals_df.iloc[r,1]})")
print("-------------------------")
print(f"Winner: {df2.iloc[0,0]}")
print("-------------------------")
output_path = os.path.join("Analysis","Results.txt")
with open(output_path, 'w') as text_file:
    text_file.write("Election Results\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Total Votes: {votercount}\n")
    text_file.write("-------------------------\n")
    for r in range(0,4):
        text_file.write(f"{totals_df.iloc[r,0]}: {totals_df.iloc[r,2]}% ({totals_df.iloc[r,1]})\n")
    text_file.write("-------------------------\n")
    text_file.write(f"Winner: {df2.iloc[0,0]}\n")
    text_file.write("-------------------------\n")