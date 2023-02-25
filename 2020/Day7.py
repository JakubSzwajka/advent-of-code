file = open("sample_data.txt", "r")

rules = []
result = 0

# does some bag1 containg bag2 ? 
def does_contain( bag_1 , bag_2 ):
    for rule in rules: 
        if rule['color'] == bag_1:
            for bag_in_bag1 in rule['contains']:
                if bag_in_bag1['color'] == bag_2:
                    return True
                else:
                    x = does_contain(bag_in_bag1['color'], bag_2)
                    if x == True:
                        return True
    return False

def get_rule_for_bag( bag ):
    for rule in rules: 
        if rule['color'] == bag: 
            return rule

# take information abount containing bags in rule
def rule_contains( bags ):
    string = ' '.join(bags)
    bags_contained = string.split(',')
    result_list = []

    for bag_contained in bags_contained: 
        bag = {}

        bag_list = bag_contained.split(' ')
        if bag_list[0] == '':
            bag_list.remove('')
        bag['color'] = bag_list[1] + ' ' + bag_list[2]
        bag['quant'] = bag_list[0]
        result_list.append(bag)

    return result_list

def how_many_bags_for_bag( bag_rule ):
    x = 0
    print(bag_rule['contains'])
    for bags_inside in bag_rule['contains']:
        if bags_inside['quant'] != 'no':
            x += int(bags_inside['quant'])
            inside_bag_rule = get_rule_for_bag(bags_inside['color'])
            if inside_bag_rule != None:
                y = int(bags_inside['quant']) * how_many_bags_for_bag(inside_bag_rule)
                x += y
    return x 

for row in file: 
    words = row.strip().split(' ')

    rule = {}
    rule['color'] = words[0] + ' ' + words[1]
    rule['contains'] = rule_contains(words[4:])
    rules.append(rule)     

# Part I result
# for rule in rules:
#     if does_contain( rule['color'], 'shiny gold'):
#         result += 1

print(how_many_bags_for_bag(get_rule_for_bag('shiny gold')))
# print(rules)