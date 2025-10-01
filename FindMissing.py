linst = [2, 1, 3, 5]

length = len(linst)
checks = [False] * (length + 1)

for i in range(0, len(linst)):
    checks[linst[i]-1] = True

for i in range(0, length + 1):
    if checks[i] == False:
        print(i+1)
        break