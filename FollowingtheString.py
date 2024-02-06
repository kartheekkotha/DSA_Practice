# Polycarp lost the string s
#  of length n
#  consisting of lowercase Latin letters, but he still has its trace.

# The trace of the string s
#  is an array a
#  of n
#  integers, where ai
#  is the number of such indices j
#  (j<i
# ) that si=sj
# . For example, the trace of the string abracadabra is the array [0,0,0,1,0,2,0,3,1,1,4
# ].

# Given a trace of a string, find any string s
#  from which it could have been obtained. The string s
#  should consist only of lowercase Latin letters a-z.
def followString(arr):
    alphabets = [chr(i) for i in range(97, 123)]
    dict = {}
    string = ''
    count = 0
    for i in arr:
        if i == 0:
            count+=1 
            dict[alphabets.pop(0)] = 0
    for i in arr:
        for j in dict:
            if i==dict[j]:
                string+=j
                dict[j]+=1
                break
    return string
t = int(input())
output = []
for i in range(t):
    n = int(input())
    arr = []
    arr = list(map(int , input().split()))
    print(followString(arr))
