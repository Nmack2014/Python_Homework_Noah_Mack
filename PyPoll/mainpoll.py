import os, csv

poll_csv = os.path.join('Resources', 'election_data.csv')
i = 0
j = 0
name = str()
counter = int()
results = []
vote_count = []
max_val = int()
max_ind = int()

with open(poll_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    vote_data = list(csv_reader)

    
    vote_data.pop(0)
    for i in range(len(vote_data) -1):
        name = vote_data[i][2]
        if name in results:
            
            i+=1
        else:
            results.append(name)
          
        i+=1
        

    for j in range(len(vote_data) -1):
        counter += vote_data[j][2].count(results[0])
        j+=1
    vote_count.append(counter)
    counter = 0
    for j in range(len(vote_data) -1):
        counter += vote_data[j][2].count(results[1])
        j+=1
    vote_count.append(counter)
    counter = 0
    for j in range(len(vote_data) -1):
        counter += vote_data[j][2].count(results[2])
        j+=1
    vote_count.append(counter)
    counter = 0
    for j in range(len(vote_data) -1):
        counter += vote_data[j][2].count(results[3])
        j+=1
    vote_count.append(counter)
    counter = 0
    max_val = max(vote_count)
    max_ind = vote_count.index(max_val)

  
print("Election Results")
print("----------------")
print("Total Votes:", len(vote_data))
print(results[0],":", ((vote_count[0]/len(vote_data))*100),"%(",vote_count[0],")")
print(results[1],":", ((vote_count[1]/len(vote_data))*100),"%(",vote_count[1],")")
print(results[2],":", ((vote_count[2]/len(vote_data))*100),"%(",vote_count[2],")")
print(results[3],":", ((vote_count[3]/len(vote_data))*100),"%(",vote_count[3],")")
print("----------------")
print("Winner: ", results[max_ind])
print("----------------")


