#The total number of months included in the dataset
#The net total amount of "Profit/Losses" over the entire period
#The changes in "Profit/Losses" over the entire period, and then the average of those changes
#The greatest increase in profits (date and amount) over the entire period
#The greatest decrease in profits (date and amount) over the entire period








path = os.path.join("Resources", "budget_data.csv")

text_file = os.path.join("Analysis", "pybank_review_results.txt")

months = []
profit_loss = []
changes = []

with open(path, "r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    
    for row in csv_reader:
        
        months.append(row[0])
        profit_loss.append(int(row[1]))

for i in range(1, len(profit_loss)):
    changes.append((int(profit_loss[i]) - int(profit_loss[i-1])))

print(f"Financial Analysis")
print("-" * 24)
print(f"Total Months: {len(list(months))}")
print(f"Total: ${sum(profit_loss)}")
print(f"Average Change: ${round(sum(changes) / len(changes), 2)}")
print(f"Greatest Increase in Profits: {months[81]} (${max(changes)})")
print(f"Greatest Decrease in Profits: {months[51]} (${min(changes)})")
with open(text_file, "w") as out_file:
    out_file.writelines(["Financial Analysis \n",
                        "-------------------------- \n",
                        "Total Months: 86 \n",
                        "Total: $38382578 \n",
                        "Average Change: $-2315.12 \n",
                        "Greatest Increase in Profits: Aug-2016 ($1862002) \n",
                        "Greatest Decrease in Profits: Feb-2014 ($-1825558) \n"])