"""
给你一个整数数组 nums ，请你将数组按照每个值的频率 升序 排序。如果有多个值的频率相同，请你按照数值本身将它们 降序 排序。 

请你返回排序后的数组。

 

示例 1：

输入：nums = [1,1,2,2,2,3]
输出：[3,1,1,2,2,2]
解释：'3' 频率为 1，'1' 频率为 2，'2' 频率为 3 。
示例 2：

输入：nums = [2,3,1,3,2]
输出：[1,3,3,2,2]
解释：'2' 和 '3' 频率都为 2 ，所以它们之间按照数值本身降序排序。
示例 3：

输入：nums = [-1,1,-6,4,5,-6,1,4,1]
输出：[5,-1,4,4,-6,-6,1,1,1]
 

提示：

1 <= nums.length <= 100
-100 <= nums[i] <= 100

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/sort-array-by-increasing-frequency
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


import collections


class Solution:
    def frequencySort(self, nums):
        s = sorted(collections.Counter(nums).items(), key=lambda a: (a[1], -a[0]))
        return [i[0] for i in s for j in range(i[1])]


if __name__ == "__main__":

    solution = Solution()

    test_cases = [
        ([1, 1, 2, 2, 2, 3], [3,1,1,2,2,2]),
        ([2,3,1,3,2], [1,3,3,2,2]),
        ([-1,1,-6,4,5,-6,1,4,1], [5,-1,4,4,-6,-6,1,1,1]),
    ]

    for num, res in test_cases:
        assert res == solution.frequencySort(num), "num:{}, res:{}".format(num, solution.frequencySort(num))


"""
知识点：Python sort

a = [1,2,4,3,5]

- list.sort()效率略大于sorted
- sorted可对任意可迭代类型使用，list.sort()只用于list
- sorted中key参数可以多级排序，将多个需要排序的内容放到一个元组中，sorted会依次从第一个开始排序
- 如果有多个相同的值，排序会保留他们原来的顺序
"""
