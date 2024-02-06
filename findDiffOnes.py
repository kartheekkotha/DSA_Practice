# def findUnique(arr, l , r):
#     val1 = l
#     val2 = -1
#     for i in range(l , r):
#         if arr[i] != arr[l-1]:
#             val2 = i+1
#             return val1 , val2
#         # for j in range(i+1 , r):
#         #     if arr[i] != arr[j]:
#         #         return i+1 , j+1
#     arr = []
#     for i in range()
#     return -1 , -1
def findUnique(arr):
    rarr = []
    i = 0
    last = 0
    while(i < len(arr)):
        if arr[i] != arr[last]:
            for _ in range(last , i):
                rarr.append(i)
            last = i
        if i == len(arr) - 1:
            for _ in range(last , i+1):
                rarr.append(-1)
        i+=1
    return rarr        
t = int(input())
for i in range(t):
    n  = int(input())
    arr = list(map(int , input().split()))
    rarr = findUnique(arr)
    q = int(input())
    for i in range(q):
        l, r = map(int , input().split())
        if rarr[l-1] == -1 or rarr[l-1] >= r:
            # print("-1 -1")
            print(f'{-1} {-1}')
        else:
            print(f'{l} {rarr[l-1]+1}')
            # print(str(l) + "" +str(rarr[l-1]+1))