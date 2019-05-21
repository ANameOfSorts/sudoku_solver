import copy
# create a board, iterate over unchecked singles, and check
# if no unchecked singles remain, look for the smallest group and split

r = [range(0,9),
     range(9,18),
     range(18,27),
     range(27,36),
     range(36,45),
     range(45,54),
     range(54,63),
     range(63,72),
     range(72,81)]

c = [range(0,81,9),
     range(1,81,9),
     range(2,81,9),
     range(3,81,9),
     range(4,81,9),
     range(5,81,9),
     range(6,81,9),
     range(7,81,9),
     range(8,81,9)]

g = [[0,1,2,9,10,11,18,19,20],
     [3,4,5,12,13,14,21,22,23],
     [6,7,8,15,16,17,24,25,26],
     [27,28,29,36,37,38,45,46,47],
     [30,31,32,39,40,41,48,49,50],
     [33,34,35,42,43,44,51,52,53],
     [54,55,56,63,64,65,72,73,74],
     [57,58,59,66,67,68,75,76,77],
     [60,61,62,69,70,71,78,79,80]]

def initialize(x):
    if int(x) == 0:
        return [1,2,3,4,5,6,7,8,9]
    else:
        return [int(x)]

def solve(s, ch_r, ch_c, ch_g):
    while True:
        s_old = copy.deepcopy(s)
        for i in range(0, 9):
            for j in range(0, 9):
                # for singletons, remove from the lists in the same row, column or 3x3 group

                if len(s[r[i][j]]) == 1 and not ch_r[r[i][j]]:
                    for k in range(0, 9):
                        if k != j and s[r[i][j]][0] in s[r[i][k]]:
                            s[r[i][k]].remove(s[r[i][j]][0])
                            if len(s[r[i][k]]) == 0:
                                return False
                    ch_r[r[i][j]] = True
                        
                if len(s[c[i][j]]) == 1 and not ch_c[c[i][j]]:
                    for k in range(0, 9):
                        if k != j and s[c[i][j]][0] in s[c[i][k]]:
                            s[c[i][k]].remove(s[c[i][j]][0])
                            if len(s[c[i][k]]) == 0:
                                return False
                    ch_c[c[i][j]] = True

                if len(s[g[i][j]]) == 1 and not ch_g[g[i][j]]:
                    for k in range(0, 9):
                        if k != j and s[g[i][j]][0] in s[g[i][k]]:
                            s[g[i][k]].remove(s[g[i][j]][0])
                            if len(s[g[i][k]]) == 0:
                                return False
                    ch_g[g[i][j]] = True

        if s == s_old:  # do until no changes are produced
            break
        
    min = 0  # we want the shortest non-singleton list
    for i in range(0, 80):
        if len(s[min]) == 1 or (len(s[i]) < len(s[min]) and len(s[i]) > 1):
            min = i

    if len(s[min]) == 1:
        return s
    elif len(s[min]) > 1:
        for num in s[min]:
            #print(num)
            #print(s[min])
            #print(min)
            #for i in range(0,9):
                #print(" ".join(map(repr, s[i*9:(i+1)*9])))
            #print()
            copy_s = copy.deepcopy(s)
            copy_r = copy.deepcopy(ch_r)
            copy_c = copy.deepcopy(ch_c)
            copy_g = copy.deepcopy(ch_g)
            copy_s[min] = [num]
            ans = solve(copy_s, copy_r, copy_c, copy_g)
            if ans:
                return ans
        return False
    else:
        raise Exception

while True:
    s = []
    checked_r = [False] * 81
    checked_c = [False] * 81
    checked_g = [False] * 81
        
    for i in range(0,9):
        s.extend(map(initialize, input().split()))

    ans = solve(s, checked_r, checked_c, checked_g)

    if ans:
        for i in range(0,9):
            print(" ".join(map(repr, ans[i*9:(i+1)*9])))
            #print(" ".join(map(repr, list(zip(*ans[i*9:(i+1)*9]))[0])))
    else:
        print("No Solution")
