import os
import csv

csv_path = os.path.join('../pypoll', 'Resources', 'election_data.csv')

with open(csv_path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    csv_header = next(csvreader)

    vote_count = []
    candidates = []
    candidate_vote_count = []
    candidate_total_votes = []
    candidate_percentage_votes = []

    for row in csvreader:
        total_votes = vote_count.append(row[0])
        candidate_vote_count.append(row[2])
        if row[2] not in candidates:
            candidates.append(row[2])

    print(len(vote_count))


    for i in range(len(candidates)):
        candidate_count = candidate_vote_count.count(candidates[i])
        candidate_total_votes.append(candidate_count)
        percentage_votes = (candidate_count / (len(vote_count))) * 100
        candidate_percentage_votes.append(round(percentage_votes, 2))

    winner = max(candidate_total_votes)
    winner_index = candidate_total_votes.index(winner)
    winning_candidate = candidates[winner_index]

    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str((len(vote_count))))
    print("-------------------------")
    print(f"{candidates[0]}: {candidate_percentage_votes[0]}% ({str(candidate_total_votes[0])})")
    print(f"{candidates[1]}: {candidate_percentage_votes[1]}% ({str(candidate_total_votes[1])})")
    print(f"{candidates[2]}: {candidate_percentage_votes[2]}% ({str(candidate_total_votes[2])})")
    print("-------------------------")
    print("Winner: " + winning_candidate)

with open('../PyPoll/analysis/output.txt', "w") as output:
    output.write(
        '\n'.join([
            "Election Results",
            "-------------------------",
            "Total Votes: "+ str((len(vote_count))),
            "-------------------------",
            f"{candidates[0]}: {candidate_percentage_votes[0]}% ({str(candidate_total_votes[0])})",
            f"{candidates[1]}: {candidate_percentage_votes[1]}% ({str(candidate_total_votes[1])})",
            f"{candidates[2]}: {candidate_percentage_votes[2]}% ({str(candidate_total_votes[2])})",
            "-------------------------",
            "Winner:  "+ winning_candidate
        ]))