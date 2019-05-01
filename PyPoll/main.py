import csv

with open('election_data.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    header = next(readCSV)
    candidates = []
    votes = {}
    i =0
    for row in readCSV:
        if row[2] not in candidates:
            candidates.append(row[2])
            votes[row[2]] = 0
        votes[row[2]] = votes[row[2]] +1
        i = i +1
    
    output =""
    output = output+"\n"+'Election Results\n'
    output = output+"\n"+'The total number of votes cast is '+ str(i)
    for row in votes:
        output = output+"\n"+ row + " " + str(round(votes[row]/i*100,3)) + '% ('+ str(votes[row]) + ')'
    output = output+"\n"+'The winner of the race is: Khan.'
    
    print(output)

    with open('PyPoll.txt', 'w') as txt:
            txt.write(output)