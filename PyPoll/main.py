# PyPoll: In this challenge, you are tasked with helping a small, rural town modernise its vote counting process.
# You will be give a set of poll data called [election_data.csv](PyPoll/Resources/election_data.csv). 
# The dataset is composed of three columns: `Voter ID`, `County`, and `Candidate`. Your task is to create a Python script that analyses the votes and calculates each of the following:
#1-The total number of votes cast
#2-A complete list of candidates who received votes
#3-The percentage of votes each candidate won
#4-The total number of votes each candidate won
#5-The winner of the election based on popular vote.

#As an example, your analysis should look similar to the one below:
# Election Results
#  -------------------------
#  Total Votes: 3521001
#  -------------------------
#  Khan: 63.000% (2218231)
#  Correy: 20.000% (704200)
#  Li: 14.000% (492940)
#  O'Tooley: 3.000% (105630)
#  -------------------------
#  Winner: Khan
#  -------------------------
# In addition, your final script should both print the analysis to the terminal and export a text file with the results.

# Dependencies
import os
import csv

# Set path for file
resource= os.path.join(os.path.expanduser("~"), "Documents/Assignments/Python-challenge/PyPoll/Resources")
csvpath = os.path.join(resource, "election_data.csv")

Total_Votes = 0
CandidateList = []
Vote_Count = []
Votes_Percent = 0.000
Output = []

# Open the CSV
with open(csvpath) as csvfile: 
    csvreader = csv.reader(csvfile, delimiter=",")
    
    #store/ skip the header row
    header = next(csvreader)

    # Loop through each row
    for row in csvreader:
        Total_Votes = Total_Votes + 1  
        Candidate = row[2]
        if not Candidate in CandidateList:
               CandidateList.append(Candidate)
               Vote_Count.append(1)
        else:
                indexofCandidate =  CandidateList.index(Candidate)
                curVoteTally = Vote_Count[indexofCandidate]
                Vote_Count[indexofCandidate] = curVoteTally+1

#print the analysis to the terminal and export a text file with the results
Analysis= os.path.join(os.path.expanduser("~"), "Documents/Assignments/Python-challenge/PyPoll/Analysis")
outputpath = os.path.join(Analysis,"Results_election_data.txt")    
results = open(outputpath, "w")
Winner_Votes = 0

#create the output
Output.append("Election Results")
Output.append("---------------------------")
Output.append("Total Votes: " + str(Total_Votes))
Output.append("---------------------------")
for Candidate in CandidateList:
    Votes = Vote_Count[CandidateList.index(Candidate)]
    Votes_Percent = (Votes/Total_Votes)*100
    if (Votes>Winner_Votes):
        Winner = Candidate
        Winner_Votes = Votes
    Output.append(Candidate +": " + str("{:.3f}".format(Votes_Percent))+"% " + " (" +str(Votes)+ ")" )
Output.append("---------------------------")
Output.append("Winner: " + Winner)
Output.append("---------------------------")

#write the output to file and console
for x in Output:
    print(x)
    print(x,file=results)
    
#close the file
results.close()