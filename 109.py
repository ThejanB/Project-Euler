def main():
    shots = []
    shots.append(('M', 0))
    for n in range(1, 21):
        shots.append((f'S{n}', n))
    shots.append(('S25', 25))
    for n in range(1, 21):
        shots.append((f'D{n}', 2*n))
    shots.append(('D25', 50))
    for n in range(1, 21):
        shots.append((f'T{n}', 3*n))

    doubles = [(lbl, val) for (lbl, val) in shots if lbl.startswith('D')]

    count = 0
    N = 100  # we want total < 100
    L = len(shots)
    for d_lbl, d_val in doubles:
        for i in range(L):
            i_val = shots[i][1]
            for j in range(i, L):
                j_val = shots[j][1]
                if i_val + j_val + d_val < N:
                    count += 1

    print(count)


main()
