file = open("sample_data.txt", "r")

preamble_length = 25
numbers = []
for row in file:
    numbers.append(int(row.strip()))

def number_validator( position, list):
    if position < preamble_length:
        # print("Cannot check preamble")
        return

    valid_flag = False
    preamble = list[position - preamble_length: position ]
    checking_numb = list[position]

    for x in range(len(preamble)):
        for y in range(len(preamble)):
            if x != y:
                if preamble[x] + preamble[y] == checking_numb:
                    valid_flag = True
    return valid_flag

def number_finder(num_list):
    for num_index in range(len(num_list)):
        if number_validator(num_index,num_list) == False:
            return num_list[num_index]
            break


def encryption_weakness_range( numb_list , wrong_num ):
    for x in range(len(numb_list)):
        sum = 0
        starting_index = x
        tmp_index = x

        while sum <= wrong_num:
            sum += numb_list[tmp_index]

            if sum == wrong_num:
                return numb_list[ starting_index : tmp_index + 1]
            tmp_index += 1

wrong_number = number_finder(numbers)
weakness_list = encryption_weakness_range( numbers, wrong_number)

weakness_list.sort()
print(wrong_number)
print(weakness_list)
print(weakness_list[0] + weakness_list[-1]) 