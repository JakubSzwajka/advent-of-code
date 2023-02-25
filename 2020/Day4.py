import re

file = open("sample_data.txt", "r")

passports = []
valid_passports = 0
obligatory_fields = ['byr', 'iyr' , 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
passport = ''

# make all passport data in one line 
for row in file: 
    passport = passport + ' ' + row.strip()

    if row.strip() == '':
        passports.append(passport)
        passport = ''
passports.append(passport)

passport_list = []

# make a dictionary
for x in passports:
    passport = {}
    field_list = x.split(' ')

    for field in field_list:
        key_value = field.split(':')
        if key_value[0] != '':
            passport[key_value[0]] = key_value[1]
    passport_list.append(passport)

# validate passport fields 
def field_validator(field, key):
    regex_color = "^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$"
    reg_color = re.compile(regex_color)

    regex_heigh = "^1[5-9][0-9]([cm]){2}$|^[5-7][0-9]([in]){2}$"
    reg_heigh = re.compile(regex_heigh)

    return {
        'byr': lambda x: True if 2002 >= int(x) >= 1920 else False, 
        'iyr': lambda x: True if 2010 <= int(x) <= 2020 else False,
        'eyr': lambda x: True if 2020 <= int(x) <= 2030 else False, 
        'hgt': lambda x: True if re.search(reg_heigh,x) else False,
        'hcl': lambda x: True if re.search(reg_color,x) else False, 
        'ecl': lambda x: True if x in colors else False,
        'pid': lambda x: True if len(str(x)) == 9 else False 
    }[key](field)
    
# check if passport has all obligatory fields and then valid them
def passport_validator( passport ):
    for obligtory_field in obligatory_fields:
        if obligtory_field not in passport.keys(): 
            return False
        else: 
            if field_validator( passport[obligtory_field] , obligtory_field) == False:
                return False
    return True

# calculate valid passports 
for passport in passport_list:
    if (passport_validator(passport)):
        valid_passports += 1

print(valid_passports)
