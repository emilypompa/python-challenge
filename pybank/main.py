
import os
import csv

csv_path = os.path.join('../pybank','Resources', 'budget_data.csv')

with open(csv_path) as csvfile:
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    month_count = []
    total = []

    for row in csvreader:
        month_count.append(row[0])
        total.append(int(row[1]))

    total_profit_loss = []
    for i in range (1, len(total)):
        profit_loss_change = total[i] - total[i-1]
        total_profit_loss.append(profit_loss_change)

    avg_change = (sum(total_profit_loss)/len(total_profit_loss))

    greatest_profit = max(total_profit_loss)
    greatest_profit_month_index = total_profit_loss.index(greatest_profit)
    greatest_profit_month = month_count[greatest_profit_month_index+1]

    greatest_loss = min(total_profit_loss)
    greatest_loss_month_index = total_profit_loss.index(greatest_loss)
    greatest_loss_month = month_count[greatest_loss_month_index + 1]

print("Financial Analysis")
print("----------------------------")
print(f"Total Months:  {len(month_count)}")
print(f"Total:  ${sum(total)}")
print(f"Average Change:  ${round(avg_change, 2)}")
print(f"Greatest Increase in Profits:  {greatest_profit_month} (${greatest_profit})")
print(f"Greatest Decrease in Profits:  {greatest_loss_month} (${greatest_loss})")

with open('../PyBank/analysis/output.txt', 'w') as output:
    output.write("Financial Analysis\n")
    output.write("----------------------------\n")
    output.write(f"Total Months:  {len(month_count)}\n")
    output.write(f"Total:  ${sum(total)}\n")
    output.write(f"Average Change:  ${round(avg_change, 2)}\n")
    output.write(f"Greatest Increase in Profits:  {greatest_profit_month} (${greatest_profit})\n")
    output.write(f"Greatest Decrease in Profits:  {greatest_loss_month} (${greatest_loss})\n")