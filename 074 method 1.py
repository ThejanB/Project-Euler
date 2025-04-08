from time import time
import math

def main():
        no_of_chains = 0
        for no in range(3,10**6):
                count = 0
                number = str(no)
                list_1 = [no]
                while count < 60:
                        tot = sum(math.factorial(int(i)) for i in number)
                        count += 1
                        if count == 60 :
                                no_of_chains += 1
                                break

                        if tot in list_1:
                                break
                        else:
                                list_1.append(tot)
                        number = str(tot)

        print(no_of_chains)

start = time()
main()
print("\n",time()-start,"seconds")
