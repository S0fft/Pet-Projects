answer_info = input("Data: ")

answer_range_key = int(input("Key - 1: "))
answer_factor_key = int(input("Key - 2: "))
answer_division_key = int(input("Key - 3: "))

latters = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
num_range_of_latter = [*range(answer_range_key, answer_range_key + (len(latters)))]

index_of_latter = [answer_factor_key * elem for elem in num_range_of_latter]

dict_num_latters = dict(zip(index_of_latter, latters))

answer_info = int(answer_info, 2)
answer_info *= answer_division_key
answer_info = str(answer_info)

step_int = 0
for i in index_of_latter:
    step_int += len(str(i))
    break

code_of_latter = 1 # Future array

code_of_latter = [int(elem) for elem in code_of_latter]

result_data = ""

for num in code_of_latter:
    for k, v in dict_num_latters.items():
        if k == num:
            result_data += v

print(result_data)
