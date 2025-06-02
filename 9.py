if __name__ == "__main__" :
    n = int(input())
    numlist = list(map(int, input().split(" ")))
    firstnum, secondnum, flag = numlist[0], numlist[0], numlist[0]
    while True:
        secondnum = numlist[numlist[secondnum]]
        firstnum = numlist[firstnum]
        if firstnum == secondnum:
            break
    while flag != firstnum:
        firstnum = numlist[firstnum]
        flag = numlist[flag]
    print(flag)

