import os
import csv

report = open('analysis/election_data_analysis.txt','w')

path = 'Resources/election_data.csv' # Path to collect data from the Resources folder
csv_file = open(path) #go down that path
csv_reader = csv.reader(csv_file) #read the csv dataset there, turning it into an array (well, list techincally) that we can read here
next(csv_file) #skip the first row of column headers

vote_counter = 0 #set initial value of vote counter
candidates = [] #set initial empty list of unique candidates
csv_reader2 = [] #set initial empty list that I'm going to copy my csv dataset into so I can re-iterate through

#this block makes the list of unique candidates, counts all the votes, and makes a duplicate of the csv so we can iterate through it again
for row in csv_reader: #for every row in this dataset
    vote_counter += 1 #add one to the counter, helping us count the total number of votes
    if row[2] in candidates: #if the candidate in that row is already in our list of unique candidates
        "" #do nothing
    else:
        candidates.append(row[2]) #but if they're aren't in the list already, put them in the list
    csv_reader2.append(row) #and then copy that row into the new blank list

total_votes_per_can = [] #this is going to be a list, parallel to the unique candidate list, counting how many votes that candidate has. So the nth element of this list will be the total number of votes that the nth person in the candidates list got
winning_vote_count = 0 #initial value for how many votes the winner got

print("Election Results")
print("~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"Total Votes: {vote_counter}")
print("~~~~~~~~~~~~~~~~~~~~~~~~~")

report.write("Election Results\n")
report.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
report.write(f"Total Votes: {vote_counter}\n")
report.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")

#this block prints out the candidates and the vote results
for i in range(len(candidates)): #we're going to iterate through our dataset, looking at one candidate at a time.
    candidate_votes = 0 #initial count of votes for that candidate
    for row in csv_reader2: #for every row in the dataset
        if row[2] == candidates[i]: #if the candidate in that row is the candidate we're looking at this time around
            candidate_votes += 1 #add one vote for them
    total_votes_per_can.append(candidate_votes) #keep doing that through the whole dataset. Once you get to the end, you've got all the votes, so you put that final vote count into the list of "final vote counts"
    
    if total_votes_per_can[i]>winning_vote_count: #if that candidate has more votes than the current most-votes-getter
        winning_vote_count = total_votes_per_can[i] #make that number of votes the new "most votes"
        winner = candidates[i] #and let that candidate become the current holder of the "winner title"
    
    percentage = round(100*int(total_votes_per_can[i])/vote_counter,3) #calc percentage of the total votes that that person got
    print(f"{candidates[i]}: {percentage}% ({total_votes_per_can[i]})")
    report.write(f"{candidates[i]}: {percentage}% ({total_votes_per_can[i]})\n")

print("~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"Winner: {winner}")
print("~~~~~~~~~~~~~~~~~~~~~~~~~")

report.write("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
report.write(f"Winner: {winner}\n")
report.write("~~~~~~~~~~~~~~~~~~~~~~~~~")

report.close()