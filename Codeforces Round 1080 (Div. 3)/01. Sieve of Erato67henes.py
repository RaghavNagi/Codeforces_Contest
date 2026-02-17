n = int(input())

for _ in range(n):
    a = int(input())
    arr = list(map(int, input().split()))

    if 67 in arr:
        print("Yes")
    else:
        print("NO")