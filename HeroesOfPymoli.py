import pandas as pd


#Read csv
csv_path = 'purchase_data.csv'
purchase_df = pd.read_csv(csv_path, encoding="utf-8")
#print(purchase_df.columns.values)
purchase_df = pd.DataFrame(purchase_df)

#Player Count
total_players = (purchase_df["Purchase ID"].count())

#Purchasing Analysis
uniq_items = (purchase_df["Item Name"])
uniq_total = len(set(uniq_items))
total_rev = (purchase_df["Price"].sum())
average = (total_rev / total_players)
num_purch = (total_players)
purch_summary = {
    "Number of Purchases": [num_purch],
    "Total Unique Items": [uniq_total],
    "Total Revenue": [total_rev],
    "Average Price": [average]
}
summary_df = pd.DataFrame(purch_summary)
#print(summary_df)

#Gender Demographics
#male = purchase_df.iloc[ : , 3]
male = purchase_df['Gender'].value_counts()['Male']
perc_male = (male / total_players) * 100
female = purchase_df['Gender'].value_counts()['Female']
perc_female = (female / total_players) * 100

print(male)
print(female)