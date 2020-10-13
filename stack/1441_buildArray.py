"""
给你一个目标数组 target 和一个整数 n。每次迭代，需要从  list = {1,2,3..., n} 中依序读取一个数字。

请使用下述操作来构建目标数组 target ：

Push：从 list 中读取一个新元素， 并将其推入数组中。
Pop：删除数组中的最后一个元素。
如果目标数组构建完成，就停止读取更多元素。
题目数据保证目标数组严格递增，并且只包含 1 到 n 之间的数字。

请返回构建目标数组所用的操作序列。

题目数据保证答案是唯一的。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/build-an-array-with-stack-operations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def buildArray(self, target, n):
        operators = []
        i, max_x = 1, target[-1]
        while i <= max_x:
            operators.append("Push")
            if i not in target:
                operators.append("Pop")
            i += 1
        return operators


if __name__ == "__main__":
    target = [1, 3]
    n = 3
    s = Solution()
    res = s.buildArray(target, n)
    print(f"test case: target={target},n={n}, result={res}")
