class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low, high = 0, len(matrix) - 1
        row_idx = 0

        while low <= high:
            mid = low + (high - low) // 2
            n = len(matrix[mid]) - 1

            if matrix[mid][0] <= target and target <= matrix[mid][n]:
                row_idx = mid
                break
            elif matrix[mid][n] > target:
                high = mid - 1
            else:
                low = mid + 1

        row = matrix[row_idx]
        low, high = 0, len(row) - 1
        while low <= high:
            mid = low + (high - low) // 2

            if row[mid] == target:
                return True
            elif row[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return False