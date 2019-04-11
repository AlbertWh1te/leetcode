# 239. Sliding Window Maximum

# Given an array nums,
#  there is a sliding window of size k which is moving from the very left of the array to the very right.
#  You can only see the k numbers in the window.
#  Each time the sliding window moves right by one position.
#  Return the max sliding window.

# Example:

# Input: nums = [1,3,-1,-3,5,3,6,7], and k = 3
# Output: [3,3,5,5,6,7]
# Explanation:

# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
# Note:
# You may assume k is always valid, 1 ≤ k ≤ input array's size for non-empty array.

# Follow up:
# Could you solve it in linear time?

from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) < 1 or len(nums) < k:
            return []
        result = [0 for _ in range(len(nums) - k + 1)]
        max_deque = deque()
        index = 0
        for i in range(len(nums)):
            while len(max_deque) != 0 and nums[i] >= nums[max_deque[-1]]:
                max_deque.pop()

            max_deque.append(i)
            if max_deque[0] == i - k:
                max_deque.popleft()

            if i >= (k - 1):
                result[index] = nums[max_deque[0]]
                index += 1
        return result


if __name__ == '__main__':
    from util import Test
    s = Solution()
    t = Test(s.maxSlidingWindow)
    # t.equal([3, 3, 5, 5, 6, 7], [1, 3, -1, -3, 5, 3, 6, 7], 3)
    t.equal([7, 4], [7, 2, 4], 2)
