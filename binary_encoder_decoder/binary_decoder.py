from binary_encoder import (answer_division_key, answer_info, dict_num_letters,
                            index_of_latter)

answer_info = int(answer_info, 2)
answer_info *= answer_division_key
answer_info = str(answer_info)

step_int = 0
for i in index_of_latter:
    step_int += len(str(i))
    break

code_of_latter = 1  # Future array

code_of_latter = [int(elem) for elem in code_of_latter]

result_data = ""

for num in code_of_latter:
    for k, v in dict_num_letters.items():
        if k == num:
            result_data += v

print(result_data)
