# approach1 
arr = [2,7,11,15]
k = 9
for i in range(len(arr)):
    for j in range(i+1 , len(arr)):
        if arr[i] + arr[j] == k:
            print(i,j)
            break
# approach2 & 3
# Use Hash Map to store the elements and their indices.