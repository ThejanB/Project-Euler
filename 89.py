file = open('89 Project Euler.Txt','r')
text_file = file.read()
text_file = text_file.split('\n')

count = 0
for x in text_file:
    a = x.replace('VIIII','IX').replace('IIII','IV').replace('LXXXX','XC').replace('XXXX','XL').replace('DCCCC','CM').replace('CCCC','CD')
    count += len(x)-len(a)
   
print(count)
