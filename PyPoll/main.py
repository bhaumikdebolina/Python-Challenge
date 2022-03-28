import os
# Module for reading CSV
import csv
csvpath = os.path.join("Resources", "election_data.csv")
print("Election Results")
print("__________________")
votes = []
candidates = []
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print (csvreader)
    header = next(csvreader)

    ## Initialize variables
    votes_cast = 0
    list_of_candidates = set()
    vote_Charles_Casper = 0
    vote_Diana_DeGette = 0
    vote_Raymon_Anthony = 0

    for column in csvreader:
        votes.append(column[0])
        candidates.append(column[2])

    Total_Votes = (len(votes))
    print(f"Total Votes: {Total_Votes}")

    #count candidates
    Charles = int(candidates.count("Charles"))
    Diana = int(candidates.count("Diana"))
    Raymon = int(candidates.count("Raymon"))

    #percentage calculation
    Charles_percentage = (Charles/Total_Votes) * 100
    Diana_percentage = (Diana/Total_Votes) * 100
    Raymon_percentage = (Raymon/Total_Votes) * 100

    #Print
    print(f"Charles: {Charles_percentage}% ({Charles})")
    print(f"Diana: {Diana_percentage}% ({Diana})")
    print(f"Raymon: {Raymon_percentage}% ({Raymon})")