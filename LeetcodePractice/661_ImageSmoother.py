# An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image 
# by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother). 
# If one or more of the surrounding cells of a cell is not present, we do not consider it in the average 
# (i.e., the average of the four cells in the red smoother).

class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        output = []
        for i in range(0 , len(img)):
            outputRow = []
            for j in range(0 , len(img[i])):
                conv = 0
                count = 0
                for a in range(i-1 , i+2):
                    if(a<0 or a >= len(img)):
                        continue
                    else:
                        for b in range(j-1 , j+2):
                            if(b<0 or b >= len(img[i])):
                                continue
                            conv+=img[a][b]
                            count+=1
                conv = conv / count
                outputRow.append(conv)
            output.append(outputRow)
        return output
        