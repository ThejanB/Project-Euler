# combinations of strings with length = 4 with L, O, A -> 3^4 = 81 
# 
# exactly following forty-three strings would lead to a prize
    # OOOO OOOA OOOL OOAO OOAA OOAL OOLO OOLA OAOO OAOA
    # OAOL OAAO OAAL OALO OALA OLOO OLOA OLAO OLAA AOOO
    # AOOA AOOL AOAO AOAA AOAL AOLO AOLA AAOO AAOA AAOL
    # AALO AALA ALOO ALOA ALAO ALAA LOOO LOOA LOAO LOAA
    # LAOO LAOA LAAO
# These provided details are actually not needed to solve the problem

# Actual Problem:
#      Given n days, find the number of ways to attend the class to get the prize
#      possible actions:
#           A - Absent, L - Late, O - On time
# Conditions to get the prize:
#       1. three consecutive A's are not allowed
#       2. two consecutive L's are not allowed
# ToDo:
#       1. Find the count of all the possible combinations



n = 30

#  memory[days][absent][late] for unique combination
memory = [[[0,0] for _ in range(3)] for _ in range(n+1) ]       # 3 is the maximum number of absent and 2 is the maximum number of late, n+1 for accessing the index from 1 to n

def count(days , absent, late):
    if late > 1:
        return 0
    if absent > 2:
        return 0
    if days == 0:
        return 1

    if memory[days][absent][late] != 0:
        return memory[days][absent][late]
    
    # No absent, No late
    temp_count = count(days - 1, 0, late)
    # No absent, Late
    temp_count += count(days - 1, 0, late + 1)
    # Absent
    temp_count += count(days - 1, absent + 1, late) 

    memory[days][absent][late] = temp_count
    
    return temp_count

print(count(n, 0, 0))
# print(memory)