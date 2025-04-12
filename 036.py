from time import time
start = time()

tot = 0
for no in range(1,10**6):
        if str(no) == str(no)[::-1]:
                binary_no = str(bin(no))
                if binary_no[2::] == binary_no[:1:-1]:
                        tot += no
print(tot)

print("\n",time()-start,'seconds')
