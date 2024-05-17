# approach 1
# store the prefix and the suffix multiplication and then multiply
arr = [1 , 2 , 3 , 4]
suffix = [1 for _ in len(arr)]
prefix = [1 for _ in len(arr)]
for i in range(1 , len(arr)):
    prefix[i] = prefix[i-1] * arr[i-1]
for i in range(len(arr)-2 , -1 , -1):
    suffix[i] = suffix[i+1] * arr[i+1]
for i in range(len(arr)):
    arr[i] = prefix[i] * suffix[i]
print(arr)

# approach 2
# store the prefix and the suffix multiplication in the same array
