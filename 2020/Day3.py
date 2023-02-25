file = open("sample_data.txt", "r")

trajectories = [[1,1],[3,1],[5,1],[7,1],[1,2]]

map = []
for row in file:
    map.append(row.strip())

def forest_trajectory( move_x , move_y ):
    x = 0
    y = 0
    trees_to_cut = 0

    for row_num in range(len(map)):
        row = map[y]
        if(row[x] == '#'):
            trees_to_cut += 1

        x = ( x + move_x ) % len(row)
        y += move_y
        if y > len(map):
            return trees_to_cut

    return trees_to_cut

result_tab = [ forest_trajectory(tra[0], tra[1]) for tra in trajectories]

result = 1
for x in result_tab:
    result *= x
print(result)
