"""
给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。

如果不能形成任何面积不为零的三角形，返回 0。

 

示例 1：

输入：[2,1,2]
输出：5
示例 2：

输入：[1,2,1]
输出：0
示例 3：

输入：[3,2,3,4]
输出：10
示例 4：

输入：[3,6,2,3]
输出：8
 

提示：

3 <= A.length <= 10000
1 <= A[i] <= 10^6

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-perimeter-triangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def largestPerimeter(self, A):
        A.sort()
        i = len(A) - 1
        while i >= 2:
            if A[i] < A[i-1] + A[i-2]:
                return A[i] + A[i-1] + A[i-2]
            i -= 1
        return 0


if __name__ == "__main__":
    s = Solution()

    test_cases = [
        ([2, 1, 2], 5),
        ([1, 2, 1], 0),
        ([3, 2, 3, 4], 10),
        ([3, 6, 2, 3], 8),
    ]

    for case, res in test_cases:
        assert s.largestPerimeter(case) == res, "case:{}, res:{}".format(case, s.largestPerimeter(case))