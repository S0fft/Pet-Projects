answer_info = input("Data: ")

answer_range_key = int(input("Key - 1: "))
answer_factor_key = int(input("Key - 2: "))
answer_division_key = int(input("Key - 3: "))

letters = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
num_range_of_latter = [*range(answer_range_key, answer_range_key + (len(letters)))]

index_of_latter = [answer_factor_key * elem for elem in num_range_of_latter]

dict_num_letters = dict(zip(index_of_latter, letters))

result_data = ""

for i in answer_info:
    for k, v in dict_num_letters.items():
        if i == v:
            result_data += str(k)

result_data = f"{bin(int(result_data) // answer_division_key)}"

print(result_data)
