# 303. Range Sum Query - Immutable

## Problem

Given an integer array nums, find the sum of the elements between indices $i$ and $j$ ($i ≤ j$), inclusive.

## Example

```
Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3
```

**Note:**
You may assume that the array does not change.
There are many calls to sumRange function.

## Solution

### Brute Force

It is the most straight way to calculate the sum of numbers from given range of an array.

```py
class NumArray:

    class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def sumRange(self, i: int, j: int) -> int:
        if j < i:
            raise Exception("j cannot smaller than i")
        res = 0
        for idx in range(i, j+1):
            res += self.nums[idx]
        return res

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)
```

This solution cost $O(1)$ on building, and cost $O(n)$ for each query.

### Difference of accumulation sum

To optimize the query performance, we spend linear time complexity during initialization. We specify an array to store the sum from the beginning to position $i$. It can be expressed as $$A(i) = \sum_k=0^i a_k$$. Therefore, the sum of range $i$ to $j$ is $$Sum(i,j) = A(j)-A(i-1)$$. As a result, each query is translated to a constant time complexity expression.

```py
class NumArray:

    def __init__(self, nums):
        self.accuSum = []
        numsSum = 0
        for num in nums:
            numsSum += num
            self.accuSum.append(numsSum)

    def sumRange(self, i: int, j: int) -> int:
        if i == 0:
            return self.accuSum[j]
        return self.accuSum[j]-self.accuSum[i-1]
```
