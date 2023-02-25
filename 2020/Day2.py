file = open("sample_data.txt", "r")


def validator( password_policy ): 
    f, s = password_policy["range"].split("-")
    letter = password_policy["letter"]
    password = password_policy["password"]
    first = int(f)
    second = int(s)

    if ( password[first - 1] == letter and password[second - 1] != letter ) or ( password[first - 1] != letter and password[second - 1] == letter ):
        return True
    else:
        return False

passwords = []
for password in file:
    pass_setting = password.split(" ")

    policy = {
        "range" : pass_setting[0],
        "letter" : pass_setting[1][0],
        "password" : pass_setting[2].strip()
    }
    passwords.append(policy)

i = 0
for password in passwords:
    if validator(password):
        i += 1

print(i)
