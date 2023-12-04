import os
import csv

election_data_csv = os.path.join("Resources", "election_data.csv")
output_file = "election_results.txt"  # Name for the output file

def PyPoll_Calcs(all_data):
    ElectionResults = int(all_data[3])
    return ElectionResults

with open(election_data_csv, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)

    total_votes = 0
    candidates = {}

    for row in csvreader:
        total_votes += 1
        candidate_name = row[2]
        if candidate_name in candidates:
            candidates[candidate_name] += 1
        else:
            candidates[candidate_name] = 1

# Print total votes,  share of votes and total votes by candidate
ElectionResults = (
    "Election Results\n"
    "_______________________________________\n"
    f"Total Votes: {total_votes}\n"
    "_______________________________________\n"
)

for candidate, votes in candidates.items():
    percentage = (votes / total_votes)
    ElectionResults += f"{candidate}: {percentage:.2%} ({votes})\n"

# Print the winner
winner = max(candidates, key=candidates.get)
ElectionResults += (
    "________________________________________\n"
    f"Winner: {winner}\n"
)

print(ElectionResults)

# results witten to output file
with open(output_file, "w") as output:
    output.write(ElectionResults)
