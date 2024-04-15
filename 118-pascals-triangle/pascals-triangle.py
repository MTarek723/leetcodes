class Solution(object):
    def generate(self, numRows):
        traingle = [[1],[1,1]]
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return traingle
        for i in range(2,numRows):
            row = []
            for j in range(0,i+1):
                if j == 0:
                    row.append(1)
                elif j == i:
                    row.append(1)
                else:
                    row.append(traingle[i-1][j-1] + traingle[i-1][j])
            traingle.append(row)
        return traingle

