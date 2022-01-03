n = int(input())
arr = map(int, input().split())

arr = sorted(arr)


def unique():
    arr_p = []
    for i in arr:
        if i not in arr_p:
            arr_p.append(i)
    print(arr_p[-2])


unique()
