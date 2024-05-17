#return the duplicates in O(1) space complexity and o(n) time
#The elements are from 0 to n-1
arr = [1 , 2 , 3 , 1 , 3 , 6 , 6]
length = len(arr)
# for i in range(length):
#     if arr[arr[i]] == 7:
#         print(arr[i])
#     else:
#         arr[arr[i]] = 7

# keep 0 and -1 as flag as looked at the next and visited
