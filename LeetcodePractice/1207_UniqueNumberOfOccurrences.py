class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        j = arr[0]
        dic = {}
        for i in arr:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        dic2 = {}
        for i in dic:
            if dic[i] in dic2 :
                return False
            else:
                dic2[dic[i]] = 1
        return True