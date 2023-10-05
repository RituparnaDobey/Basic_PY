# Print the sum of the current number and the previous number


for i in range(10):
    if i == 0:
        current_num = i
        previous_num = 0
    else:
        current_num = i
        previous_num = i - 1


    sum_of_numbers = current_num + previous_num

    print(f"current_num:{current_num}, previous_num:{previous_num},sum_of_numbers:{sum_of_numbers}")



# for i in range(10):
#     if i == 0:
#         current_number = i
#         previous_number = 0
#     else:
#         current_number = i
#         previous_number = i - 1
        
#     sum_of_numbers = current_number + previous_number
#     print(f"The sum of {current_number} and {previous_number} is: {sum_of_numbers}")
