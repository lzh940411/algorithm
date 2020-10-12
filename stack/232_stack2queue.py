"""
使用栈实现队列的下列操作：

push(x) -- 将一个元素放入队列的尾部。
pop() -- 从队列首部移除元素。
peek() -- 返回队列首部的元素。
empty() -- 返回队列是否为空。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-queue-using-stacks
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stackin = []
        self.stackout = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stackin.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stackout:
            while self.stackin:
                self.stackout.append(self.stackin.pop())
        return self.stackout.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.stackout:
            while self.stackin:
                self.stackout.append(self.stackin.pop())
        return self.stackout[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if not self.stackin and not self.stackout:
            return True
        else:
            return False

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
