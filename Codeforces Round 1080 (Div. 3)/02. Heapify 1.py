n = int(input())

for _ in range(n):
    a = int(input())
    arr = [0] + list(map(int, input().split()))

    changed = True
    while changed:
        changed = False
        for i in range(1, a // 2 + 1):
            if arr[i] > arr[2 * i]:
                arr[i], arr[2 * i] = arr[2 * i], arr[i]
                changed = True

    if all(arr[i] >= arr[i - 1] for i in range(2, a + 1)):
        print("YES")
    else:
        print("NO")