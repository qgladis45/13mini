a = input().split(',')
n = int(a[0])       # 找出小於等於n的質數
k = int(a[1])       # 小於等於n的k倍數


def prime(x):
    check = 1
    for i in range(2, int(x)):
        if x % i == 0:
            check = 0
            break
    if check == 1:
        return(True)   # 是質數
    else:
        return(False)  # 不是質數

if k == 1:
    print('1,2', end='')
else:
    print(2, end='')

for i in range(3, n+1):
    printyes = False
    if prime(i) is True:
        printyes = True

    if i % k == 0:
        printyes = True

    if printyes is True:
        print(',', end='')
        print(i, end='')