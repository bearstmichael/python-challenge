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
new_list = []

for row in csv_reader: #for every row in our dataset
    if month_count > 0: #if we're not in the first row of data
        changes.append(int(row[1])-last_month) #subtract what's in the second column from last month's second column. This is the change from month to month. Put each of these successive differences into a list

    month_count += 1 #add 1 to the number of months we've looked at
    running_total += int(row[1]) #add this running total
    last_month = int(row[1]) #this month's total? Just remember that for now, next month I'll ask you what it is so that we can see what the change was.
    new_list.append(row)

print(new_list)

# running_changes_total=0
# greatest_increase = changes[0]
# greatest_decrease = changes[0]

# for change in changes: #for each of the values of a the list of successive differences
#     running_changes_total += change #add them up one at a time, in a running total
#     if change > greatest_increase: #if you find a change that's bigger than the so-far-biggest change
#         greatest_increase = change #...replace it as the biggest change
#     if change < greatest_decrease: #if you find a change that's smaller than the so-far-smallest change
#         greatest_decrease = change #...replace it as the smallest change

# average = round(running_changes_total/(month_count-1),2) #the average is that running total divided by the number of months (less one, b/c 86 months only have 85 changes from one month to the next)

# print(f"Total Months: {month_count}")
# print(f"Total: ${running_total}")
# print(f"Average Change: ${average}")


# #for some reason, I'm having a hard time extracting the month that corresponds to the greatest inc/dec
# #I'm not sure why this doesn't work:
# greatest_month=""
# least_month=""
# for row in new_list:
#     if int(row[1]) == int(greatest_increase):
#         greatest_month = str(row[0])
#     if int(row[1]) == int(greatest_decrease):
#         least_month = str(row[0])

# print(f"Greatest Increase: {greatest_month} (${greatest_increase})")
# print(f"Greatest Decrease: {least_month} (${greatest_decrease})")