import os
# Module for reading CSV
import csv
csvpath = os.path.join("Resources", "election_data.csv")
print("Election Results")
print("__________________")
#votes = []
#candidates = []
electionData = []
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    #print (csvreader)
    header = next(csvreader)

    ## Initialize variables
    #votes_cast = 0
    #list_of_candidates = set()
    #vote_Charles_Casper = 0
    #vote_Diana_DeGette = 0
    #vote_Raymon_Anthony = 0

    for column in csvreader:
        #votes.append(column[0])
        #candidates.append(column[2])
        electionData.append(column)

    Total_Votes = (len(electionData))
    print(f"Total Votes: {Total_Votes}")

    #count candidates
    Charles = len([i for i in electionData if i[2] == "Charles Casper Stockham"])
    Diana = len([i for i in electionData if i[2] == "Diana DeGette"])
    Raymon = len([i for i in electionData if i[2] == "Raymon Anthony Doane"])
   # total_candidates = len(set([i[2] for i in electionData]))
    
    #percentage calculation
    Charles_percentage = (Charles/Total_Votes) * 100
    Diana_percentage = (Diana/Total_Votes) * 100
    Raymon_percentage = (Raymon/Total_Votes) * 100

    #Print
    print(f"Charles: {Charles_percentage}% ({Charles})")
    print(f"Diana: {Diana_percentage}% ({Diana})")
    print(f"Raymon: {Raymon_percentage}% ({Raymon})")

    #choose winner
    if Charles > Diana > Raymon:
        Winner = "Charles"
    elif Diana > Charles > Raymon:
        Winner = "Diana"
    elif Raymon > Charles > Diana:
        Winner = "Raymon"
    print (f"Winner: {Winner}")