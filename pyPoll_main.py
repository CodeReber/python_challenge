import os
import csv

csvpath = os.path.join('PyPoll', 'Resources','election_data.csv')

data = csv.DictReader(open(csvpath))
candidates = []
total_voters = 0
Khan = 0
Correy = 0
Li = 0
Otooley = 0
for d in data:
    voterid = str(d['Voter ID'])
    cans = str(d['Candidate'])
    total_voters += 1
    if cans not in candidates:
        candidates.append(cans)
    if candidates[0] in cans:
        Khan += 1
    elif candidates[1] in cans:
        Correy += 1
    elif candidates[2] in cans:
        Li += 1
    elif candidates[3] in cans:
        Otooley += 1

print(Khan)
print(Correy)
print(Li)
print(Otooley)
print(f'Election Results\n')
print(f'--------------------------')
print(f'Total Votes:  {total_voters}')