import os
import csv

# read our data
path = 'Resources/budget_data.csv'
csv_file = open(path)
csv_reader = csv.reader(csv_file)

next(csv_file)

month_count = 0
running_total = 0
changes = []
this_month = 0
last_month = 0
csv_reader2 = []

#this block is how I construct the list of 'changes in profit/losses'; find the total amount of money/months; copy data to new dataset we can iterate through again
for row in csv_reader: #for every row in our dataset
    if month_count > 0: #if we're not in the first row of data
        changes.append(int(row[1])-last_month) #subtract what's in the second column from last month's second column. This is the change from month to month. Put each of these successive differences into a list

    month_count += 1 #add 1 to the number of months we've looked at
    running_total += int(row[1]) #add this running total
    last_month = int(row[1]) #this month's total? Just remember that for now, next month I'll ask you what it is so that we can see what the change was.
    csv_reader2.append(row)

running_changes_total=0
greatest_increase = changes[0]
greatest_decrease = changes[0]
row_idx=0
greatest_row_idx = 0
least_row_idx = 0

#this is the row where I figure out which months have the greatest/least change
for change in changes: #for each of the values of a the list of successive differences
    running_changes_total += change #add them up one at a time, in a running total
    if change > greatest_increase: #if you find a change that's bigger than the so-far-biggest change
        greatest_increase = change #...replace it as the biggest change
        greatest_row_idx = row_idx + 1 #stamp that row number as containing the greatest change
    if change < greatest_decrease: #if you find a change that's smaller than the so-far-smallest change
        greatest_decrease = change #...replace it as the smallest change
        least_row_idx = row_idx + 1 #stamp that row number as containing the least change
    row_idx += 1 #add to the row counter

average = round(running_changes_total/(month_count-1),2) #the average is that running total divided by the number of months (less one, b/c 86 months only have 85 changes from one month to the next)

print("Financial Analysis")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"Total Months: {month_count}")
print(f"Total: ${running_total}")
print(f"Average Change: ${average}")

greatest_month=""
least_month=""

new_row_idx = 0 #this ticker is going to count through the rows, this is our initial value
for row in csv_reader2: #for every row in our dataset (the copied one, b/c we already iterated through the original)
    if new_row_idx == greatest_row_idx: #if the number of this row is the same as the number of the row I previously identified as containing the greatest change,
        greatest_month = str(row[0]) #stamp the greatest month as that month
    if new_row_idx == least_row_idx: #same for least month
        least_month = str(row[0])
    new_row_idx +=1 #add one to the row ticker

print(f"Greatest Increase: {greatest_month} (${greatest_increase})")
print(f"Greatest Decrease: {least_month} (${greatest_decrease})")