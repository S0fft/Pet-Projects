answer_info = input("Data: ")
print(answer_info)
answer_range_key = int(input("Key - 1: "))
answer_start_action_key = int(input("Key - 2: "))
answer_final_action_key = int(input("Key - 3: "))

latters = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")
num_of_latter = [*range(answer_range_key, answer_range_key + (len(latters)))]
print(num_of_latter)

num_of_latter = [answer_start_action_key * elem for elem in num_of_latter]
print(num_of_latter)

dict_num_latters = dict(zip(num_of_latter, latters))
print(dict_num_latters)

result_data = ""

for i in answer_info:
    for k, v in dict_num_latters.items():
        if i == v:
            result_data += str(k)

print(result_data)
result_data = f"{bin(int(result_data) // answer_final_action_key)}"

print(result_data)
