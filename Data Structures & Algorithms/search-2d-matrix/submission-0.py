
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def searchFirstIndices(left, right):
            if left > right:
                return right

            mid = (left + right) // 2

            if matrix[mid][0] == target:
                return mid

            elif matrix[mid][0] < target:
                return searchFirstIndices(mid + 1, right)

            else:
                return searchFirstIndices(left, mid - 1)

        def searchArray(array, left, right):
            if left > right:
                return False

            mid = (left + right) // 2

            if array[mid] == target:
                return True

            elif target < array[mid]:
                return searchArray(array, left, mid - 1)

            else:
                return searchArray(array, mid + 1, right)

        row = searchFirstIndices(0, len(matrix) - 1)

        if row < 0:
            return False

        return searchArray(matrix[row], 0, len(matrix[row]) - 1)
