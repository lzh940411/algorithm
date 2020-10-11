"""
给定两个 没有重复元素 的数组 nums1 和 nums2 ，其中nums1 是 nums2 的子集。找到 nums1 中每个元素在 nums2 中的下一个比其大的值。

nums1 中数字 x 的下一个更大元素是指 x 在 nums2 中对应位置的右边的第一个比 x 大的元素。如果不存在，对应位置输出 -1 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/next-greater-element-i
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def nextGreaterElement1(self, nums1, nums2):
        res = []
        for query in nums1:
            idx = nums2.index(query)
            if idx != len(nums2) - 1:
                found = -1
                for target in nums2[idx + 1:]:
                    if target > query:
                        res.append(target)
                        found = 1
                        break
                if found == -1:
                    res.append(-1)
            else:
                res.append(-1)
        return res

    def nextGreaterElement1_2(self, nums1, nums2):
        res = []
        for query in nums1:
            ans = -1
            for target in nums2[nums2.index(query):]:
                if target > query:
                    ans = target
                    break
            res.append(ans)
        return res

    def nextGreaterElement2(self, nums1, nums2):
        res = []
        for query in nums1:
            res.append(-1)
            for target in nums2[::-1]:
                if target > query:
                    res[-1] = target
                if target == query:
                    break
        return res

    def nextGreaterElement3(self, nums1, nums2):
        stack, hashmap = list(), dict()
        for i in nums2:
            while stack and stack[-1] < i:
                hashmap[stack.pop()] = i
            stack.append(i)
        return [hashmap.get(i, -1) for i in nums1]


if __name__ == "__main__":
    test_cases = [
        ([4, 1, 2], [1, 3, 4, 2]),
        ([2, 4], [1, 2, 3, 4]),
    ]

    s = Solution()

    for nums1, nums2 in test_cases:
        res = s.nextGreaterElement1_2(nums1, nums2)
        print(f"nums1={nums1}, nums2={nums2}, result={res}\n")
