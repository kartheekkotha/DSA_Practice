# Alice has n balloons arranged on a rope. You are given a 0-indexed string colors where colors[i] is the color of the ith balloon.

# Alice wants the rope to be colorful. She does not want two consecutive balloons to be of the same color, so she asks Bob for help. Bob can remove some balloons from the rope to make it colorful. You are given a 0-indexed integer array neededTime where neededTime[i] is the time (in seconds) that Bob needs to remove the ith balloon from the rope.

# Return the minimum time Bob needs to make the rope colorful.


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        tempArr = []
        minCount = 0
        flag = False
        for i in range(1,len(colors)):
            if(colors[i]==colors[i-1]):
                tempArr.append(neededTime[i-1])
                flag = True
            else:
                if flag:
                    tempArr.append(neededTime[i-1])
                flag = False
                maxim = 0
                if(tempArr != []):
                    print(tempArr)
                    print(i , minCount)
                    maxim = max(tempArr)
                for j in tempArr:
                    minCount += j
                minCount-=maxim
                tempArr = []
        if flag:
            tempArr.append(neededTime[-1])
        flag = False
        maxim = 0
        if(tempArr != []):
            print(tempArr)
            print(i , minCount)
            maxim = max(tempArr)
        for j in tempArr:
            minCount += j
        minCount-=maxim
        tempArr = []
        return minCount