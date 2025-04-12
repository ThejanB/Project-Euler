from time import time
start = time()

file = open("059 Project Euler.Txt","r")
number_list = file.read().split(",")

def is_valid(xor):
    if 32 <= xor <= 93:         # A to Z and symbols
        return True
    elif 97 <= xor <= 122:      # a to z
        return True
    return False

list_1 = []     # for 1st key
list_2 = []     # for 2nd key
list_3 = []     # for 3rd key
for i in range (len(number_list)):
    if i%3 == 0:
        list_1.append(int(number_list[i]))
    elif i%3 == 1:
        list_2.append(int(number_list[i]))
    else:
        list_3.append(int(number_list[i]))

correct_key = ""
correct_list = []
for list_i in [list_1,list_2,list_3]:
    for key in range(97,123):
        xor_list = []
        for i in list_i:
            if is_valid(key^i)== 1:
                xor_list.append(key^i)
            else:
                break
        else:
            correct_list.append(xor_list)
            correct_key += chr(key)
            break

print("key = ",correct_key)
print("sum = ",sum(correct_list[0])+sum(correct_list[1])+sum(correct_list[2]))

'''
# print message
message = ''
for i in range(len(list_1)):
    message += chr(correct_list[0][i])
    message += chr(correct_list[1][i])
    message += chr(correct_list[2][i])
print("\nmessage -> \n",message)
'''

print("\n",time()-start,"seconds")
