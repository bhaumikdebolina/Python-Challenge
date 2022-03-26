import os
# Module for reading CSV
import csv
#set path for file
mypath = 'C:/Users/User/Desktop/python_challenge/PyBank/Resources'
csvpath = os.path.join(mypath, 'budget_data.csv')
#csvpath = os.path.join("Resources", "budget_data.csv")
my_data = []
#open the CSV 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print (csvreader)
    header = next(csvreader)
    for row in csvreader:
        my_data.append (row)

     

# create the variables to work
rows = 0
total = 0
profit = 0
Loss = 0
row_profit = 0
row_loss = 0
max = 0
min = 0


# creating variables to calculate the average change

data = []
total_profit_losses = 0
total_months = 0
total_months_list = []
Profit_change_list = []
greatest_increase = 0
greatest_decrease = 0


# Calculate the total month by Loop

for r in data:
     total_months_list.appened(row[0])
total_months = len(total_months_list)
print("Financial Analysis")
print ("...............................")
print("Total Months:", total_months)
print (data)
