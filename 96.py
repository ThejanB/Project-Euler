from time import time
start = time()

file = open('C:/Users/DELL/Desktop/Python (Euler)/96 Project Euler.Txt','r')
text = file.read().split('\n')
file.close()

puzzles = []
L       = []
for i in text:
    try:
        L.append(list(map(int,list(i))))
    except ValueError:
        puzzles.append(L)
        L = []
puzzles.append(L)
puzzles = puzzles[1::]      #puzzles = [puzzle 1,puzzle 2... ] , puzzle 1 = [ [raw 1],[raw 2]...,[raw 9] ]

def find_candidates(i,j):
    return list(set(range(1, 10))-set( puzzle[i]+[puzzle[r][j] for r in range(9)]+[puzzle[r][c] for r in range(i//3*3,i//3*3+3) for c in range(j//3*3,j//3*3+3)] ))

def solve():
    global puzzle    
    while 0  in [n for i in range(9) for n in puzzle[i] ]:
        middle_break = False            # to run the programme from begining after getting an answer
        for i in range(9):              # i for  raw
            for j in range(9):          # j for column
                if puzzle[i][j] == 0:
                    can = find_candidates(i,j)
                    len_can = len(can)
                    if len_can == 0: 
                        return False
                    elif len_can == 1:
                        puzzle[i][j] = can[0]
                        middle_break = True
                        break
            if middle_break:
                break
        else:
            t_list = []
            for u in range(3):
                for v in range(3):
                    t = [(r,c) for r in range(u*3,u*3+3) for c in range(v*3,v*3+3) if puzzle[r][c] == 0 ]
                    t_list.append(t)
            for t in range(len(t_list)):
                t_list[t] = [(r,c,find_candidates(r,c)) for r,c in t_list[t]]

            middle_break_2 = False
            for t in t_list:
                for u in t:
                    v = list(set(u[2]) - set([j for i in t for j in i[2] if i!=u]))
                    if len(v) == 1:
                        puzzle[u[0]][u[1]] = v[0]
                        middle_break_2 = True
                        break
                if middle_break_2:
                    break
            else:
                return 'Fail'
    return True

def resolve(puzzle):
    for i in range(9):                  # i for  raw
        for j in range(9):              # j for column
            if puzzle[i][j]==0:
                can = find_candidates(i,j)
                for num in can:
                    puzzle[i][j] = num
                    ans = resolve(puzzle)
                    if ans:
                        return True
                    puzzle[i][j]=0
                else:
                    return False
    return True

def print_puzzle(puzzle):
    ''' Output the puzzle    '''

    N = 9
    print()
    print('----'*N + '-')
    for i in range(N):
        print('| ',end="")
        for j in range(N):
            print(puzzle[i][j] , end=' | ' )
        print()
        print('----'*N + '-')
    print()

ans = 0
for puzzle in puzzles:
    s = solve()
    if not s:
        print('Cannot Solve')
    elif s == True:
        pass
    else:
        resolve(puzzle)

    #for z in puzzle:
    #    print(z)
    #print()

    print_puzzle(puzzle)

    ans += puzzle[0][0]*100+puzzle[0][1]*10+puzzle[0][2]

print(ans)
print(time()-start,'seconds')

'''
we can get the answer without def solve()
we can use resolve(puzzle) only to solve the puzzle 
but it takes much more time

def solve() reduse time significantly

_Mr.T_ -> 2021-05-20
'''
    
