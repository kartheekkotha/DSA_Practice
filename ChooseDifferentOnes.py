# Given an array a
#  of n
#  integers, an array b
#  of m
#  integers, and an even number k
# .

# Your task is to determine whether it is possible to choose exactly k2
#  elements from both arrays in such a way that among the chosen elements, every integer from 1
#  to k
#  is included.

# For example:

# If a=[2,3,8,5,6,5]
# , b=[1,3,4,10,5]
# , k=6
# , then it is possible to choose elements with values 2,3,6
#  from array a
#  and elements with values 1,4,5
#  from array b
# . In this case, all numbers from 1
#  to k=6
#  will be included among the chosen elements.
# If a=[2,3,4,5,6,5]
# , b=[1,3,8,10,3]
# , k=6
# , then it is not possible to choose elements in the required way.
# Note that you are not required to find a way to choose the elements — your program should only check whether it is possible to choose the elements in the required way.
def chooseDiffOnes(n , m , arr1 , arr2 , k):
    dic1 = {}
    dic2 = {}
    value = []
    for i in range(1 , k+ 1):
        dic1[i] = 0
        dic2[i] = 0
    for j in arr1:
        if j <= k:
            dic1[j]+=1
    for m in arr2:
        if m <= k:
            dic2[m]+=1
    count1 = 0
    count2 = 0
    # print(dic1)
    # print(dic2)
    for i in range(1 , k+1):
        if dic1[i] == 0:
            if dic2[i] == 0:
                return "NO"
            else:
                if(count2 == k//2):
                    # print("caught")
                    return "NO"
                count2+=1
                dic2[i]-=1
        elif dic2[i] == 0:
            if dic1[i] == 0:
                return "NO"
            else:
                if(count1 == k//2):
                    return "NO"
                count1+=1
                dic1[i]-=1
        else:
            value.append(i)
            # if count1 <= count2:
            #     count1+=1
            #     dic1[i]-=1
            # else:
            #     count2+=1
            #     dic2[i]-=1
    for i in value:
        if dic1[i] == 0:
            if dic2[i] == 0:
                return "NO"
            else:
                if(count2 == k//2):
                    return "NO"
                count2+=1
                dic2[i]-=1
        elif dic2[i] == 0:
            if dic1[i] == 0:
                return "NO"
            else:
                if(count1 == k//2):
                    return "NO"
                count1+=1
                dic1[i]-=1
        else:
            if count1 <= count2:
                count1+=1
                dic1[i]-=1
            else:
                count2+=1
                dic2[i]-=1
    return "YES"
t = int(input())
for i in range(t):
    n, m, k = map(int , input().split())
    arr1 = []
    arr1 = list(map(int , input().split()))
    arr2 = []
    arr2 = list(map(int , input().split()))
    print(chooseDiffOnes(n , m , arr1 , arr2 , k))