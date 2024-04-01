import os
import csv

# Define the path to CSV:
file_path = '/Users/christopherduke/python-challenge/PyPoll/Resources/election_data.csv'

#create a list
ballot_id = []

#Dim variables
stockham = 0
degette = 0
doane = 0
total_votes = 0
# Open the CSV 
with open(file_path) as csv_file:
    # Create a CSV reader object
    csv_reader = csv.reader(csv_file)

    # Read the header row
    csv_header = next(csv_reader)

    #loop through each row in CSV
    for rows in csv_reader:
        ballot_id.append(rows[0])
       
       # store the number of total votes
        total_votes +=1

        # count and store the number of votes per candidate
        if rows[2] == "Charles Casper Stockham":
            stockham += 1
        elif rows[2] == "Diana DeGette":
            degette +=1
        elif rows[2] == "Raymon Anthony Doane":
            doane +=1
        
#find the percentage of vote for each candidate
stockham_vote = (stockham / total_votes) * 100
deguette_vote = (degette / total_votes) * 100
doane_vote = (doane / total_votes) * 100

#name the winner 
if stockham_vote > doane_vote and stockham_vote > deguette_vote:
    winner = "Charles Casper Stockham"
elif deguette_vote > doane_vote and deguette_vote > stockham_vote:
    winner = "Diana DeGette"
else:
    winner = "Raymon Anthony Doane"


#print the results
print("Election results")
print("--------------------------")
print("Total votes: " + str(len(ballot_id)))
print("--------------------------")
print(f"Charles Casper Stockham   {round(stockham_vote, 3)}% ({stockham})")
print(f"Diana DeGette   {round(deguette_vote, 3)}% ({degette})")
print(f"Raymon Anthony Doane  {round(doane_vote, 3)}% ({doane})")
print("--------------------------")
print ("Winner: " + winner)
print("--------------------------")

# create txt file with the results
output_file = '/Users/christopherduke/python-challenge/PyPoll/analysis/election.txt'
with open(output_file, "w") as file:
    file.write("Election results")
    file.write(("\n"))
    file.write("--------------------------")
    file.write(("\n"))
    file.write("Total votes: " + str(len(ballot_id)))
    file.write(("\n"))
    file.write("--------------------------")
    file.write(("\n"))
    file.write(f"Charles Casper Stockham   {round(stockham_vote, 3)}% ({stockham})")
    file.write(("\n"))
    file.write(f"Diana DeGette   {round(deguette_vote, 3)}% ({degette})")
    file.write(("\n"))
    file.write(f"Raymon Anthony Doane  {round(doane_vote, 3)}% ({doane})")
    file.write(("\n"))
    file.write("--------------------------")
    file.write(("\n"))
    file.write ("Winner: " + winner)
    file.write(("\n"))
    file.write("--------------------------")