file = open("sample_data.txt", "r")

nums = []
for num in file:
    nums.append(num.strip())

def day1( numbers):  
    length = len(numbers)
    for x in range(length):
        for y in range(length): 
            for z in range(length):
                int_a = int(numbers[x])
                int_b = int(numbers[y])
                int_c = int(numbers[z])
                if int_a + int_b + int_c == 2020: 
                    return int_a * int_b * int_c
                  
print(day1(nums))