# Given a log file of user_id, timestamp & page visited find the 10 most common triplets, where a triplet is an occurrence of 3 pages visited sequentially by the same user.
# Log file format is assumed to be csv
from csv import reader


# Save triplets and last 3 pages each user visited as dictionaries
triplets = {}
last_visited = {}

with open('log.csv') as file:
    data = reader(file)
    # Order data by timestamp
    data = sorted(data, key = lambda row: row[1])

    for row in data:
        # Add last visited page to list in dict with key user
        try:
            current_user_history = last_visited[row[0]]
            if len(current_user_history) < 3:                
                current_user_history.append(row[2])
            else:
                current_user_history[0] = current_user_history[1]
                current_user_history[1] = current_user_history[2]
                current_user_history[2] = row[2]
        except KeyError:
            last_visited[row[0]] = list()
            last_visited[row[0]].append(row[2])
            continue
        
        # Count triplet
        # If it's not in triplets, then set value to 1, else add 1
        if len(current_user_history) == 3:
            current_triplet = tuple(current_user_history)
            if current_triplet in triplets:
                triplets[current_triplet] += 1
            else:
                triplets[current_triplet] = 1

# Get list of 10 triplets with most appearences
triplets = sorted(triplets.items(), key = lambda item: item[1], reverse=True)[:10]
print("10 most common triplets:")
for triplet in triplets:
    print(f"{triplet[0]} | Times: {triplet[1]}")
