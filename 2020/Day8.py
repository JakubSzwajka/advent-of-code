import copy

file = open("sample_data.txt", "r")

instructions = []

terminate_correctly = False
accumulator = 0
last_index_global = 0 

# make a list of dicts 
for row in file:
    instruction = {}
    parts = row.strip().split(' ')
    instruction['inst'] = parts[0]
    instruction['step'] = int(parts[1])
    instruction['times'] = 0
    instructions.append(instruction)

instr_quant = len(instructions)

# validate if instruction list is ok
def boot_validator( instructions ):
    accumulator = 0
    iterator = 0
    terminate_correctly = False 

    while instructions[iterator]['times'] == 0: 

        if instructions[iterator]['inst'] == 'nop':
            instructions[iterator]['times'] += 1
            iterator += 1

            if iterator >= instr_quant:
                terminate_correctly = True
                break
            continue
        elif instructions[iterator]['inst'] == 'acc':
            instructions[iterator]['times'] += 1
            accumulator += instructions[iterator]['step']
            iterator += 1
            
            if iterator >= instr_quant:
                terminate_correctly = True
                break
            continue

        elif instructions[iterator]['inst'] == 'jmp':
            instructions[iterator]['times'] += 1
            iterator += instructions[iterator]['step']
            
            if iterator >= instr_quant:
                terminate_correctly = True
                break
            continue

        if iterator == len(instructions):
            terminate_correctly = True

    return accumulator , terminate_correctly

# change instruction "nop" <-> "jmp" starting from index
def change_instructions( i_list, i_index ):

    for instr in i_list[i_index:]:
        i_index += 1  

        if instr['inst'] != 'acc' and (instr['inst'] != 'nop' or instr['step'] != 0):
    
            instr['inst'] = {
                'jmp' :lambda x: 'nop',
                'nop' :lambda x: 'jmp'
            }[instr['inst']](instr['step'])

            break 
    return i_list, i_index

x = copy.deepcopy(instructions)
while terminate_correctly == False:
    accumulator , terminate_correctly = boot_validator(x)
    print(str(accumulator) + ' terminate correctly: ' + str(terminate_correctly))
    print(x)

    if terminate_correctly == False: 
        x, last_index_global = change_instructions(copy.deepcopy(instructions), last_index_global)
    else:
        print("sukces! Akumulator na końcu to: " + str(accumulator))
    if last_index_global == 9:
        break

