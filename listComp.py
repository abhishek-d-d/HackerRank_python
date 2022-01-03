X = int(input())
Y = int(input())
Z = int(input())
N = int(input())

res = [[i, j, k] for i in range(X + 1) for j in range(Y + 1) for k in range(Z + 1) if i + j + k != N]
print (res)

'''
def list_res(a, b, c):
    abcde = []
    if (a + b + c) != n:
        for i in range(0, a + 1):
            for j in range(0, b + 1):
                for k in range(0, c + 1):
                    abcde.extend([[i, j, k]])
    print(abcde)


list_res(x, y, z)
'''
