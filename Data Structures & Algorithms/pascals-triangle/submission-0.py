class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = [[1] * (i + 1) for i in range(numRows)]

        for i in range(numRows):
            for j in range(len(triangle[i])):
                if j != 0 and j != len(triangle[i]) - 1:
                    triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

        return triangle