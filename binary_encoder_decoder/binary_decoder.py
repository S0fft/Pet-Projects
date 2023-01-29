answer_info = input("Data: ")  # 0b11001111111110101000111111010010001011101001110001100010100000100101011001000111010000100101100

answer_range_key = int(input("Key - 1: "))  # 7
answer_factor_key = int(input("Key - 2: "))  # 3
answer_division_key = int(input("Key - 3: "))  # 2

latters = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
num_of_latter = [*range(answer_range_key, answer_range_key + (len(latters)))]

index_of_latter = [answer_factor_key * elem for elem in num_of_latter]

answer_info = int(answer_info, 2)
answer_info *= answer_division_key
answer_info = list(str(answer_info))

step = 0

for i in index_of_latter:
    step += len(str(i))
    break

code_of_latter = []
for i in range(0, len(answer_info)):
    pass

code_of_latter = [int(elem) for elem in code_of_latter]

dict_num_latters = dict(zip(index_of_latter, latters))

result_data = ""

for num in code_of_latter:
    for k, v in dict_num_latters.items():
        if num == k:
            result_data += v

print(result_data)
