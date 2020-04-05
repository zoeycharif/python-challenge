#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.

import os
import csv


votes = [] 
total_votes = 0 
candidates = []
unique_list = [] 
vote_per_candidate = 0
winner = 0 

with open('election_data.csv') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

     # skip first row .
    csv_header = next(csvreader)

    #start for loop 
    # create counter for total votes
    for row in csvreader:
        total_votes += 1
        
    # complete list of candidates who received votes

        candidates = row[2]   #3rd column provides names of candidates 
        votes.append(candidates)
        if unique_list.count(candidates) == 0:  #if the name of a candidate doesn't appear
                unique_list.append(candidates)   #then add it to the unique_list
   
print('\nElection Results')
print('----------------------')
print('Total Votes:'+str(total_votes))

for i in unique_list:
    print('Candidate: '+ str(i) + '{:.3f}'.format(votes.count(i)/total_votes*100) + '% (' + str(votes.count(i)) +')')
    if winner < votes.count(i):
        winner = votes.count(i)
        winner_name = i

print('Winner: ' + winner_name)


f= open("Election Results.txt","w+")
f.write('\nElection Results\n')
f.write('---------------------\n')
f.write('Total Votes:'+str(total_votes)+'\n')

for i in unique_list:
    f.write('Candidate: '+ str(i) + '{:.3f}'.format(votes.count(i)/total_votes*100) + '% (' + str(votes.count(i)) +')\n')
 
#f.write('Candidate:'+ str(i) + ' (' + str(votes.count(i)/total_votes*100) +')'+'\n')
f.write('Winner:' + winner_name)

#('Average Change: $' + str(format(average_change,".2f")))
#Election Results
#-------------------------
#Total Votes: 3521001
#-------------------------
#Khan: 63.000% (2218231)
#Correy: 20.000% (704200)
#Li: 14.000% (492940)
#O'Tooley: 3.000% (105630)
#-------------------------
#Winner: Khan
#-------------------------
