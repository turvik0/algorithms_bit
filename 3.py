list1,list2 = [], []
num = int(input())
list1.append(3*num+10)
def scheme(i, final, num):
    print(f'GATE {final} AND {i} {i+num}')
    print(f'GATE {final+1} OR {i} {i+num}')
    print(f'GATE {final+2} NOT {final}')
    print(f'GATE {final+3} AND {final+1} {final+2}')
    print(f'GATE {final+4} AND {final+1} {i+2*num}')
    print(f'GATE {final+5} OR {final+4} {final}')
    list1.append(final+5)
    #---------------------------------------------------
    print(f'GATE {final+6} AND {final+2} {final+4}')
    print(f'GATE {final+7} NOT {final+6}')
    print(f'GATE {final+8} OR {final+3} {i+2*num}')
    print(f'GATE {final+9} AND {final+7} {final+8}') 
    list2.append(final+9)
    #---------------------------------------------------
    if i == 0:
        print(f'GATE {final+10} AND {final+7} {final+6}')
        return 11
    return 10
#------------------------------
final = 3*num
for j in range(num):
    step = scheme(j, final, num)
    final += step
list2.append(3*num+10)
#---------------------------------
for i, j in enumerate(list2):
    print(f'OUTPUT {i} {j}')
for i, j in enumerate(list1):
    print(f'OUTPUT {num+1+i} {j}')