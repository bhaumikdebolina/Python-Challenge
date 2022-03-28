import os
# Module for reading CSV
import csv
#set path for file
#mypath = 'C:/Users/User/Desktop/python_challenge/PyBank/Resources'
#csvpath = os.path.join(mypath, 'budget_data.csv')
csvpath = os.path.join("Resources", "budget_data.csv")
#my_data = []
#open the CSV 
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print (csvreader)
    header = next(csvreader)
    #for row in csvreader:
        #my_data.append (row)

     
# Initialize variables
    rows = 0
    total = 0
    Profit = 0
    Loss = 0
    row_profit = 0
    row_loss = 0
    Max = 0
    Min = 0

    # Initialize variables to calculate the average change between months
    Profit_Loss_change = 0
    Total_Profit_Loss_list = []
    Month_change = 0
    Profit_Loss_change_list = []
    Total_months_list = []
    current_Profit_Loss = 0
    last_Profit_Loss = 0

    # Loop through the data

    for row in csvreader:
        rows += 1

        total = total + int(row[1])

        if (int(row[1]) > 0):
            Profit = Profit + int(row[1])
            row_profit += 1
        else:
            Loss = Loss + int(row[1])
            row_loss += 1

        # Find the average in "Profit/Losses" between months over the entire period

        Total_months_list.append(row[0])
        Total_Profit_Loss_list.append(int(row[1]))



            # Find Greatest increase and decrease in profits (date and amount) over the entire period

        if (int(row[1]) > Max):
            Max = int(row[1])
            Month_max = row[0]
        elif (int(row[1]) < Min):
            Min = int(row[1])
            Month_min = row[0]
        
    for i in range(len(Total_Profit_Loss_list) - 1):
        Profit_Loss_change_list.append(Total_Profit_Loss_list[i + 1] - Total_Profit_Loss_list[i])
        
        Average_change = sum(Profit_Loss_change_list) / len(Profit_Loss_change_list)
        
        
        
    
    


 #Print the analysis
print("Financial Analysis")
print("-----------------------\n")
print("Total Months", Total_months_list)
print(f"Total: {str(total)}\n")
print(f"Average Change: {str('%.2f' % Average_change)}\n")
Greatest_Increase_Profits = max(Profit_Loss_change_list)
Greatest_Decrease_Profits = min(Profit_Loss_change_list)
print(Greatest_Increase_Profits), Total_months_list
print(Greatest_Decrease_Profits), Total_months_list

