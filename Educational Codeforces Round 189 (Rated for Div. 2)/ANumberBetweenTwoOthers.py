t = int(input())  # number of test cases

for _ in range(t):

    x, y = map(int, input().split())

    flag = False
    k = 2
    while k*x < y:
        z = k*x
        if z%y!= 0:
            flag = True
            break
        k+=1
    
    if flag:
        print("YES")
    else:
        print("NO")
