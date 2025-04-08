def is_increasing(i):
    for j in range(len(i)-1):
        if i[j] > i[j+1]:
            return 0
    return 1
            
def is_decreasing(i):
    for j in range(len(i)-1):
        if i[j] < i[j+1]:
            return 0
    return 1            
    
def is_bouncy(i):
    if is_increasing(i) == 1:
        return 0
    if is_decreasing(i) == 1:
        return 0
    return 1

i = 100
bouncy = 0
percentage = 0.0
while percentage < .99:
    i += 1
    if is_bouncy(str(i)) == 1:
        bouncy += 1
        percentage = bouncy/i

print('bouncy =',bouncy,', i = ',i,', percentage =',percentage,'%')
