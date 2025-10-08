list = [2, 1, 5, 4]

def find_missing_number(list):
    length = len(list)
    checks = [False] * (length + 1)

    for i in range(0, len(list)):
        checks[list[i]-1] = True

    for i in range(0, length + 1):
        if checks[i] == False:
            print(i+1)
            break

def findmissingnum2(list):
    length = len(list)
    return ((length + 1) * (length + 2) // 2) - sum(list)

def main():
    find_missing_number(list)
    print(findmissingnum2(list))

main()