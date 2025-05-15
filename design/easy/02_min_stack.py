"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-easy/98/design/562/
Title: Min Stack
Official difficulty: Easy
Real difficulty: 7/10

Description:
    Design a stack that supports push, pop, top, and retrieving the minimum element
    in constant time.

    Implement the MinStack class:
    * MinStack() initializes the stack object.
    * void push(int val) pushes the element val onto the stack.
    * void pop() removes the element on the top of the stack.
    * int top() gets the top element of the stack.
    * int getMin() retrieves the minimum element in the stack.

    You must implement a solution with O(1) time complexity for each function.

Example 1:
    Input:
        ["MinStack","push","push","push","getMin","pop","top","getMin"]
        [[],[-2],[0],[-3],[],[],[],[]]

    Output:
        [null,null,null,null,-3,null,0,-2]

    Explanation:
        MinStack minStack = new MinStack();
        minStack.push(-2);
        minStack.push(0);
        minStack.push(-3);
        minStack.getMin(); // return -3
        minStack.pop();
        minStack.top();    // return 0
        minStack.getMin(); // return -2

Constraints:
    -2^31 <= val <= 2^31 - 1
    Methods pop, top and getMin operations will always be called on non-empty stacks.
    At most 3 * 10^4 calls will be made to push, pop, top, and getMin.
"""


class MinStack:

    def __init__(self):
        self._stack = []
        self._min_stack = []

    def push(self, val: int) -> None:
        """
        The idea is, because we can only add and remove items from the stack from the right,
        the min stack only needs to know what min value to return depending on the length of
        the stack. For example, if I push 1, 2, 3, 0, 9, the min stack will stay 1, 1, 1, 0, 0
        because the min is 0, but if we pop the 9 the min is still 0, and if we pop the 0 then
        the min is 1. This is why we append the min of current min and new min in min_stack.
        """
        self._stack.append(val)
        self._min_stack.append(min(val, self._min_stack[-1] if self._min_stack else val))

    def pop(self) -> None:
        self._stack.pop()
        self._min_stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min_stack[-1]


class MinStack_v2_better:

    def __init__(self):
        self._stack = []
        self._min_stack = []

    def push(self, val: int) -> None:
        """
        The idea is, because we can only add and remove items from the stack from the right,
        the min stack only needs to know what min value to return depending on the length of
        the stack. For example, if I push 1, 2, 3, 0, 9, the min stack will stay 1, 0
        because the min is 0, but if we pop the 9 the min is still 0, and if we pop the 0 then
        we remove the 0 from the stack, and the min becomes 1. Note this works for repeated numbers
        like 2, 1, 1, 3, 0, 0, where min_stack will be 2, 1, 1, 0, 0 to ensure that on pop, we still
        have the next repeated number in min_stack
        """
        self._stack.append(val)
        if len(self._min_stack) == 0 or val <= self._min_stack[-1]:
            self._min_stack.append(val)

    def pop(self) -> None:
        val = self._stack.pop()
        if val == self._min_stack[-1]:
            self._min_stack.pop()

    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min_stack[-1]


class MinStack_MinNotConstant:

    def __init__(self):
        self._max_size = 10
        self._stack = [None] * self._max_size
        self.size = 0

    def _double_max_size(self):
        self._stack.extend([None] * self._max_size)
        self._max_size *= 2

    def push(self, val: int) -> None:
        self._stack[self.size] = val
        self._size += 1
        if self._size == self._max_size:
            self._double_max_size()

    def pop(self) -> None:
        if self.size > 0:
            self.size -= 1

    def top(self) -> int:
        if self.size > 0:
            return self._stack[self.size - 1]
        return None

    def getMin(self) -> int:
        """Not constant time."""
        return min(self._stack[:self.size])


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
