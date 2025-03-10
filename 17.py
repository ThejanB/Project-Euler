import time
start = time.time()

# method 1
units = ['','one','two','three','four','five','six','seven','eight','nine'] #10 numbers
teens = ['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen'] #10 numbers
tens_10x = ['','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety'] #9 numbers
hundreds_100x = ['','onehundred','twohundred','threehundred','fourhundred','fivehundred','sixhundred','sevenhundred','eighthundred','ninehundred']
thousand = 'onethousand'

# (10-19)+100x ->  [added 3 for 'and'] [reduce 3*10 for and(10-19)]  
a = sum(len(x+y)+3 for x in teens for y in hundreds_100x) - 3*10

# (1-9),(20-99)}+100x -> [added 3 for 'and'] [reduce 3*9 for (100-900)and] [reduce 3*90) for and(0-9),(20-99)]
b = sum(len(x+y+z)+3 for x in units for y in tens_10x for z in hundreds_100x) - 3*9 - 3*90

# thousend
c = len(thousand)

print('Total letters = ' , a+b+c)
print(time.time()-start , 'seconds')
