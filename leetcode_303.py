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