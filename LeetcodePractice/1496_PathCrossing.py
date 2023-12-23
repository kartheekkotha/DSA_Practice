# Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit north, south, east, or west, respectively. 
# You start at the origin (0, 0) on a 2D plane and walk on the path specified by path.

# Return true if the path crosses itself at any point, that is, if at any time you are on a location you have previously visited. Return false otherwise.

class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        hist = {(0,0)}
        point = [0,0]
        for i in path:
            if i == "N":
                point[1]+=1 
            elif i == "S":
                point[1]-=1
            elif i == "E":
                point[0]+=1
            else:
                point[0]-=1
            if tuple(point) in hist:
                return True
            else:
                hist.add(tuple(point))
        return False