"""
给出由小写字母组成的字符串 S，重复项删除操作会选择两个相邻且相同的字母，并删除它们。

在 S 上反复执行重复项删除操作，直到无法继续删除。

在完成所有重复项删除操作后返回最终的字符串。答案保证唯一

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-all-adjacent-duplicates-in-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def removeDuplicates(self, S: str) -> str:
        alphabets = []
        for char in S:
            if alphabets and char == alphabets[-1]:
                alphabets.pop()
            else:
                alphabets.append(char)
        return ''.join(alphabets)


if __name__ == "__main__":
    test_cases = ["abbaca", "ababbabaab"]
    solution = Solution()

    for case in test_cases:
        res = solution.removeDuplicates(case)
        print(f"test case:{case}, result:{res}")
