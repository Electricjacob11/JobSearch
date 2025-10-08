linst = [2, 1, 5, 4]

def find_missing_number(linst):
    length = len(linst)
    checks = [False] * (length + 1)

    for i in range(0, len(linst)):
        checks[linst[i]-1] = True

    for i in range(0, length + 1):
        if checks[i] == False:
            print(i+1)
            break

def findmissingnum2(linst):
    length = len(linst)
    return ((length + 1) * (length + 2) // 2) - sum(linst)

def main():
    find_missing_number(linst)
    print(findmissingnum2(linst))

main()