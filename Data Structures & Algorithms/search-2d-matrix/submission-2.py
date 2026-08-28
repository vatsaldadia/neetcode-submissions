class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        m_left, m_right = 0, m - 1
        n_left, n_right = 0, n - 1
        while n_left <= n_right:
            # print(f"{n_left=}, {n_right=}")
            n_left_ele, n_right_ele = matrix[n_left][-1], matrix[n_right][0]
            if n_left_ele == target or n_right_ele == target:
                return True
            if n_left_ele > target and n_right_ele < target:
                while m_left < m_right:
                    mid = (m_left + m_right) // 2
                    mid_ele = matrix[n_left][mid]
                    # print(f"{m_left=}, {m_right=}, {mid=}, {mid_ele=}")
                    if mid_ele == target:
                        return True
                    elif mid_ele < target:
                        m_left += 1
                    else:
                        m_right -= 1
                return False
            else:
                if n_left_ele < target:
                    n_left += 1
                if n_right_ele > target:
                    n_right -= 1
        return False