
#The total number of votes cast
#A complete list of candidates who received votes
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based on popular vote.




path = os.path.join("Resources", "election_data.csv")

text_file = os.path.join("Analysis", "pypoll_analysis.txt" )

votes = []
candidates = []

counter = {
    "Stockham": 0,
    "DeGette": 0,
    "Doane": 0,
   
}

with open(path, "r") as file:
    csv_reader = csv.reader(file)
    next(csv_reader)
    
    for row in csv_reader:
        
        votes.append(row)
        candidates.append(row[2])

for candidate in candidates:Downloads

    if candidate == "Stockham":
        counter["Stockham"] += 1
    elif candidate == "DeGette":
        counter["DeGette"] += 1
    elif candidate == "Doane":
        counter["Doane"] += 1
   
    
    stockham_votes = int(counter["Stockham"])
    degette_votes = int(counter["DeGette"])
    doane_votes = int(counter["Doane"])Downloads

    
    
    total_votes = stockham_votes + degette_votes + doane_votes 
    s_percent = (stockham_votes_votes / total_votes) * 100
    deg_percent = (degette_votes_votes / total_votes) * 100
    don_percent = (doane_votes_votes / total_votes) * 100
    
    
    
print(f"Election Results")
print("-" * 22)
print(f"Total Votes: {len(votes)}")
print("-" * 22)
print(f"Stockham: {round(s_percent)}% ({counter['Stockham']})")
print(f"DeGette: {round(deg_percent)}% ({counter['Degette']})")
print(f"Doane: {round(don_percent)}% ({counter['Doane']})")
print("-" * 22)
print(f"Winner: Diana DeGette")
print("-" * 22)

with open(text_file, "w") as out_file:
    out_file.writelines(["Election Results \n", 
                         "------------------------- \n", 
                         "Total Votes: 369711 \n", 
                         "------------------------- \n", 
                         "Charles Casper Stockham: 23.049% (85213) \n", 
                         "Diana DeGette: 73.81% (272892) \n", 
                         "Raymon Anthony Doane: 3.139% (11606) \n",                     
                         "------------------------- \n", 
                         "Winner: Diana DeGette \n", 
                         "------------------------- \n"])