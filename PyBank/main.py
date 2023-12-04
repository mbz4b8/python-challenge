import os
import csv

budgetData_csv = os.path.join("Resources", "budget_data.csv")
output_file = "financial_analysis.txt"  # Name for the output file

def PyBank_Calcs(all_data):
    ProfitLosses = int(all_data[1])
    return ProfitLosses

with open(budgetData_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    total_months = 0
    net_total = 0
    changes = []
    dates = []

    for row in csvreader:
        total_months += 1
        net_total += PyBank_Calcs(row)
        dates.append(row[0])  # Assuming date is in the first column
        changes.append(PyBank_Calcs(row))

    # Calculate differences between changes
    diff = [changes[i + 1] - changes[i] for i in range(len(changes) - 1)]

    # Calculate average change
    avg_change = sum(diff) / len(diff)

    # Find greatest increase and decrease in profits
    max_increase = max(diff)
    max_decrease = min(diff)

    # Get the corresponding dates for max increase and decrease
    max_increase_date = dates[changes.index(changes[diff.index(max_increase) + 1])]
    max_decrease_date = dates[changes.index(changes[diff.index(max_decrease) + 1])]

    # Prepare the results in a string
    results = (
        "Financial Analysis\n"
        "______________________________________\n"
        f"Total Months: {total_months}\n"
        f"Total: ${net_total}\n"
        f"Average Change: ${avg_change:.2f}\n"
        f"Greatest Increase in Profits: {max_increase_date} (${max_increase})\n"
        f"Greatest Decrease in Profits: {max_decrease_date} (${max_decrease})\n"
    )

    # Print the results
    print(results)

    # Write the results to a text file
    with open(output_file, "w") as output:
        output.write(results)