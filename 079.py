file = open('79 Project Euler.Txt','r')
keylogs = file.read().split('\n')

no = []
for key in keylogs:
    for i in key:
        if i not in no:
            no.append(i)
 
def change_index(i):
    global no,key
    a = no.index(key[i])
    if no.index(key[i-1])>a:
        no.remove(key[i-1])
        no.insert(a,key[i-1])

def password(key):
    global no
    if no.index(key[0])<no.index(key[1])<no.index(key[2]):
        return True
    change_index(1)         # if no.index(key[0])>no.index(key[1]) 
    change_index(2)         # if no.index(key[1])>no.index(key[2]) 
        
for key in keylogs:
    password(key)

shortest_password = ''
for x in no:                    # change list to str
    shortest_password += x

print("shortest password is  = ",shortest_password) 
