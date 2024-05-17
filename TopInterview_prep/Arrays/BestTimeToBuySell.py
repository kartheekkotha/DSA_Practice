'''
Given an array prices[] of length N, representing the prices of the stocks on different days, the task is to find the maximum profit possible by buying and selling the stocks on different days when at most one transaction is allowed.
'''

#Understanding 
# we find the indexes of the lesser value and the lrger value and we find the difference between the two and we return the max difference
arr = [7,1,5,3,6,4]
# approach 2 Greedy
minimum = arr[0]
maxProfit = 0
for i in range(1 , len(arr)):
    if arr[i] < minimum:
        minimum = arr[i]
    elif arr[i] - minimum > maxProfit:
        maxProfit = arr[i] - minimum
print(maxProfit)


# approach 3 Dynamic Programming
