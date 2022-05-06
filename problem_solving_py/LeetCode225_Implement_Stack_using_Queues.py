# https://leetcode.com/problems/implement-stack-using-queues/

from typing import Optional


class MyStack:

    queue1, queue2 = None, None

    def __init__(self):
        self.queue1 = []
        self.queue2 = []

    def push(self, x: int) -> None:
        self.queue1.append(x)

    def pop(self) -> int:
        for i in range(len(self.queue1) - 1):
            self.queue2.append(self.queue1.pop(0))
        self.queue1, self.queue2 = self.queue2, self.queue1
        return self.queue2.pop(0)

    def top(self) -> int:
        return self.queue1[-1] if len(self.queue1) > 0 else None

    def empty(self) -> bool:
        if len(self.queue1) > 0:
            return False
        else:
            return True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


if __name__ == "__main__":
    stack = MyStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    print(stack.pop())
    print(stack.empty())
    print(stack.pop())
    print(stack.pop())
    print(stack.top())
    print(stack.pop())
    print(stack.top())
    print(stack.empty())
