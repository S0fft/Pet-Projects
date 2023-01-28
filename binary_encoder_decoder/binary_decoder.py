answer_info = int("0b110110010101001000001100000001111100000", 2)
print(answer_info)  # 466692211680

answer_range_key = int(input("Key - 1: "))
answer_start_action_key = int(input("Key - 2: "))
answer_final_action_key = int(input("Key - 3: "))

result = (answer_info * answer_final_action_key) // answer_start_action_key
print(result)

latters = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")
num_of_latter = [*range(answer_range_key, answer_range_key + (len(latters)))]

# dict_num_latters = dict(zip(num_of_latter, latters))
# print(dict_num_latters)

# result_data = ""

# for i in answer_info:
#     for k, v in dict_num_latters.items():
#         if i == v:
#             result_data += str(k)

# result_data = int(result_data) * answer_final_action_key

# print(result_data)
