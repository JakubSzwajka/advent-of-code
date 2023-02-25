file = open("sample_data.txt", "r")

groups = []
group = []
result = 0

for line in file: 
    if line.strip() != '':
        group.append(line.strip())
    else: 
        groups.append(group)
        group = []
groups.append(group)

common = {}

for group in groups:
    if len(group) == 1:
        result += len(group[0])
    else:
        for person_index in range(len(group)): 
            if person_index == 0: 
                common = group[person_index]
            else:
                common = list(set(group[person_index]) & set(common))
        result += len(common)

print(result)
