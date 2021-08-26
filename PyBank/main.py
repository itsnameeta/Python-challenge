## PyBank: In this challenge, you are tasked with creating a Python script for analysing the financial records of your company. 
# You will give a set of financial data called [budget_data.csv](PyBank/Resources/budget_data.csv). 
# The dataset is composed of two columns: `Date` and `Profit/Losses`. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

# Your task is to create a Python script that analyses the records to calculate each of the following:
    # 1-The total number of months included in the dataset
    # 2-The net total amount of "Profit/Losses" over the entire period
    # 3-The average of the changes in "Profit/Losses" over the entire period
    # 4-The greatest increase in profits (date and amount) over the entire period
    # 5-The greatest decrease in losses (date and amount) over the entire period

# As an example, your analysis should look similar to the one below:
# Financial Analysis
#  ----------------------------
#  Total Months: 86
#  Total: $38382578
#  Average  Change: $-2315.12
#  Greatest Increase in Profits: Feb-2012 ($1926159)
#  Greatest Decrease in Profits: Sep-2013 ($-2196167)
#  In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# Dependencies
import os
import csv

# Set path for file
resource= os.path.join(os.path.expanduser("~"), "Documents/Assignments/Python-challenge/PyBank/Resources")
csvpath = os.path.join(resource, "budget_data.csv")

Total_Months = 0 
Total = 0
Average_Change = 0
Greatest_ProfIncrease_amt = 0
Greatest_ProfDecrease_amt = 0
Greatest_ProfIncrease_date = "Date"
Greatest_ProfDecrease_date = "Date"
Output = []
PrevAmount = 0
AmtIncrease = 0
AmtChange = 0.00

# Open the CSV
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    #store/ skip the header row
    header = next(csvreader) 
    
    if header != None:
    # Loop through each row after header
        for row in csvreader:
            Total_Months = Total_Months + 1
            Total = Total + int(row[1])
        
            if PrevAmount != 0:
                AmtIncrease = int(row[1]) - PrevAmount       
            AmtChange = AmtChange + AmtIncrease
            PrevAmount =  int(row[1])    

            if(AmtIncrease > Greatest_ProfIncrease_amt):
                Greatest_ProfIncrease_amt = AmtIncrease
                Greatest_ProfIncrease_date = row[0]
            
            if(AmtIncrease < Greatest_ProfDecrease_amt):
                Greatest_ProfDecrease_amt = AmtIncrease
                Greatest_ProfDecrease_date = row[0]

        Average_Change = round(AmtChange/(Total_Months-1),2)

#print the analysis to the terminal and export a text file with the results
Analysis= os.path.join(os.path.expanduser("~"), "Documents/Assignments/Python-challenge/PyBank/Analysis")
outputpath = os.path.join(Analysis,"Results_budgetdata.txt")    
results = open(outputpath, "w")
    
#create the output
Output.append("Financial Analysis")
Output.append("------------------")
Output.append("Total Months: " + str(Total_Months))
Output.append("Total: $" + str(Total))
Output.append("Average Change: $" + str(Average_Change))
Output.append("Greatest Increase in Profits : " + str (Greatest_ProfIncrease_date) + " ($" + str(Greatest_ProfIncrease_amt) + ")")
Output.append("Greatest Decrease in Profits : " + str (Greatest_ProfDecrease_date) + " ($" + str(Greatest_ProfDecrease_amt) + ")")

#write the output to file and console
for x in Output:
    print(x)
    print(x,file=results)       
    
#close the file
results.close()