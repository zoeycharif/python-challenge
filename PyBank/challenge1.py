# our task is to create a Python script that analyzes the records to calculate each of the following:
#1. The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The average of the changes in "Profit/Losses" over the entire period
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in losses (date and amount) over the entire period
#As an example, your analysis should look similar to the one below:


# open csv file on python, read it 

import os
import csv
import statistics

profit_and_losses = []              
Total_PL = 0
date = []
months = 0                         
prev_month = 0
difference = 0
difference_list = []
total_diff = 0
greatest_decrease = 0
greatest_increase = 0
#current_pl = []


with open('budget_data.csv') as csvfile:
#with open(file_path) as csvfile:      
    csvreader = csv.reader(csvfile, delimiter = ",")

    # skip first row .
    csv_header = next(csvreader)

    #Start loop. For Row in csv reader 
    for row in csvreader:
        #Create counter for months. current_row = current_row + 1
 
        months += 1
       

        #create variable for profit and losses. column2 = profit_and_losses. need to indicate it's an integer


        current_pl = int(row[1])
        
        profit_and_losses.append(current_pl)

        #calculate the result of all profit and losses
        Total_PL = Total_PL + current_pl

        
        if months > 1:
            difference =  current_pl - prev_month
            difference_list.append(difference)
            total_diff = total_diff + difference


        # greatest increase

        if (months > 1) & (difference > greatest_increase):
            greatest_increase = difference
            greatest_increase_month = row[0]

        # greatest dec

        if (months > 1) & (difference < greatest_decrease):
            greatest_decrease = difference
            greatest_decrease_month = row[0]


        prev_month = current_pl
            

    
#print('\n')
#print('')
#print("Total Months:" + str(months)
#print(Total_PL)
#print(profit_and_losses)
# print(difference_list)
# calc the average difference
average_change = statistics.mean(difference_list)

#print(average_change)
#print(greatest_increase, greatest_decrease)
#print(greatest_increase_month, greatest_increase)
#print(greatest_decrease_month,greatest_decrease)
#print('\n')

print('\nFinancial Analysis')
print('----------------------------')
print('Total Months: ' + str(months))
print('Total: $' + str(Total_PL))
print('Average Change: $' + str(format(average_change,".2f")))
print('Greatest Increase in Profits: '+ greatest_increase_month + ' ($' + str(greatest_increase) + ')')
print('Greatest Decrease in Profits: '+ greatest_decrease_month + ' ($' + str(greatest_decrease) + ')\n')


f= open("Financial Analysis.txt","w+")
f.write('----------------------------\n')
f.write('Total Months: ' + str(months)+'\n')
f.write('Total: $' + str(Total_PL)+'\n')
f.write('Average Change: $' + str(format(average_change,".2f"))+'\n')
f.write('Greatest Increase in Profits: '+ greatest_increase_month + ' ($' + str(greatest_increase) + ')'+'\n')
f.write('Greatest Decrease in Profits: '+ greatest_decrease_month + ' ($' + str(greatest_decrease) + ')\n') 
