"""
Url: https://leetcode.com/explore/interview/card/top-interview-questions-easy/98/design/670/
Title: Shuffle an Array
Official difficulty: Easy
Real difficulty: 5/10

Description:
    Given an integer array nums, design an algorithm to randomly shuffle the array.
    All permutations of the array should be equally likely as a result of the shuffling.

    Implement the Solution class:
    * Solution(int[] nums) Initializes the object with the integer array nums.
    * int[] reset() Resets the array to its original configuration and returns it.
    * int[] shuffle() Returns a random shuffling of the array.

Example 1:
    Input:
        ["Solution", "shuffle", "reset", "shuffle"]
        [[[1, 2, 3]], [], [], []]
    Output:
        [null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

    Explanation:
        Solution solution = new Solution([1, 2, 3]);
        solution.shuffle();    // Shuffle the array [1,2,3] and return a result.
                               // Any permutation must be equally likely.
                               // Example: return [3, 1, 2]
        solution.reset();      // Reset to [1,2,3]. Return [1, 2, 3]
        solution.shuffle();    // Return a random shuffle. Example: [1, 3, 2]

Constraints:
    1 <= nums.length <= 50
    -10^6 <= nums[i] <= 10^6
    All the elements of nums are unique.
    At most 10^4 calls in total will be made to reset and shuffle.
"""

from typing import List
from random import randint


class Solution:

    def __init__(self, nums: List[int]):
        self._original = nums
        self._array = self._original.copy()

    def reset(self) -> List[int]:
        self._array = self._original.copy()
        return self._array

    def shuffle(self) -> List[int]:
        n = len(self._array)
        shuffled = []
        while n > 0:
            idx = randint(0, n - 1)
            shuffled.append(self._array.pop(idx))
            n -= 1
        self._array = shuffled
        return self._array

    def shuffle_in_place(self) -> List[int]:
        n = len(self._array)
        for i in range(n):
            idx = randint(i, n - 1)
            self._array[i], self._array[idx] = self._array[idx], self._array[i]
        return self._array


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()


# validate randomness
if __name__ == "__main__":
    x = [1, 2, 3, 4, 5]
    sum_shuffle1 = [0] * len(x)
    sum_shuffle2 = [0] * len(x)
    obj = Solution(x)
    reps = 100000
    for i in range(reps):
        array1 = obj.reset()
        assert sum([elx - ely for elx, ely in zip(x, array1)]) == 0

        array2 = obj.shuffle()
        for i, n in enumerate(array2):
            sum_shuffle1[i] += n

        array3 = obj.shuffle_in_place()
        for i, n in enumerate(array3):
            sum_shuffle2[i] += n

    sum_shuffle1 = [x / reps for x in sum_shuffle1]
    sum_shuffle2 = [x / reps for x in sum_shuffle2]
    mean_x = sum(x) / len(x)
    err_shuffle1 = [f"{x - mean_x:0.5f}" for x in sum_shuffle1]
    err_shuffle2 = [f"{x - mean_x:0.5f}" for x in sum_shuffle2]
    print(err_shuffle1)  # see how close the sum of every column is to the average
    print(err_shuffle2)  # see how close the sum of every column is to the average
