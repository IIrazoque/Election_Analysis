#1. The total number of votes cast
#2. A complete list of candidated who orecieved votes
#3. The percentge of votes each candidate wom
#4. The total number of votes each candiate won
#5. The winner of the election based on popular vote

#add dependencies
# Add our dependencies.
import csv
import os

# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

#voter counter variable
total_votes = 0

#candidate options
candidate_options = []

#declare an empty dic
candidate_votes = {}

#Winning Candidate and Wining Count
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)


    # Read and print the header row.
    headers = next(file_reader)
    
    for row in file_reader:
        total_votes +=1
        candidate_name = row[2]

        # If the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            #create each candidate as a KEY
            candidate_votes[candidate_name] = 0
            #add a vote to each candidated count
        candidate_votes[candidate_name] += 1
        
    with open(file_to_save, "w") as txt_file:
            election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)
        
    for candidate_name in candidate_votes:
        votes = candidate_votes[candidate_name]
        vote_percentage = float(votes) / float(total_votes) * 100

            #print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    # Winning Candidate and Winning Count Tracker
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            winning_count = votes
            winning_percentage = vote_percentage
            winning_candidate = candidate_name
                

    #print the wining candidates results
    #winning_candidate_summary = (
       # f"---------------------------\n"
       # f"Winner: {winning_candidate}\n"
       # f"Winning Vote Count: {winning_count:.1f}%\n"
       # f"Winning Percentage: {winning_percentage:.1f}%\n"
       # f"---------------------------\n")


    print(winning_candidate_summary)
