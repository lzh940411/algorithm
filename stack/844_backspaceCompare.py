"""
给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。

注意：如果对空文本输入退格字符，文本继续为空。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/backspace-string-compare
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        stack_s, stack_t = [], []
        for s in S:
            if stack_s and s == '#':
                stack_s.pop()
            elif s != '#':
                stack_s.append(s)
        for t in T:
            if stack_t and t == '#':
                stack_t.pop()
            elif t != '#':
                stack_t.append(t)
        return stack_s == stack_t


if __name__ == "__main__":
    test_cases = [
        ("ab#c", "ad#c"),
        ("ab##", "c#d#"),
        ("a##c", "#a#c"),
        ("a#c", "b"),
    ]

    s = Solution()

    for S, T in test_cases:
        res = s.backspaceCompare(S, T)
        print(f"test case:{S, T}, result:{res}")
