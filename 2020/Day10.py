file = open("sample_data.txt", "r")

adapters_list = []

for row in file: 
    adapters_list.append(int(row.strip()))

adapters_list.sort()

adapters_list.insert(0,0)
adapters_list.append(adapters_list[-1] + 3)

size = len(adapters_list)
combos_up_to_index = [1] * size

for i in range( 1, size): 
    combos_up_to_index[i] = combos_up_to_index[ i - 1]
    if i > 1 and adapters_list[i] - adapters_list[i-2] <= 3: 
        combos_up_to_index[i] += combos_up_to_index[i - 2]
    if i > 2 and adapters_list[i] - adapters_list[i-3] <= 3:
        combos_up_to_index[i] += combos_up_to_index[i - 3]

print(adapters_list)
print(combos_up_to_index[-1])