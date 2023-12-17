# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
# typically using all the original letters exactly once.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        tdict = {}
        for i in s:
            if i in sdict:
                sdict[i]+=1 
            else:
                sdict[i] =1
        for i in t:
            if i in tdict:
                tdict[i]+=1
            else:
                tdict[i] = 1
        if(len(sdict)!= len(tdict)):
            return False
        print(sdict)
        print(tdict)
        for i in sdict.keys() :
            if i in tdict.keys():
                if sdict[i] != tdict[i]:
                    return False
            else:
                return False
        return True
            