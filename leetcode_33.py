class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Initialize left and right pointer to the start and the end
        i, j = 0, len(nums)-1
        # Terminate condition where lower pointer has moved to the left of upper pointer
        while i <= j:
            # Check whether lower pointed, upper pointed, or the middle one is the target
            # Check lower
            if nums[i] == target:
                return i
            # Check upper
            elif nums[j] == target:
                return j
            # Check middle
            mid = (i+j)//2
            if nums[mid] == target:
                return mid
            
            # If left half is ascending
            if nums[i] < nums[mid]:
                # Target is between this range
                if target > nums[i] and target < nums[mid]:
                    j = mid-1
                else:
                    i = mid+1
            # Otherwise, the right half is ascending
            else:
                # Target is between this range
                if target > nums[mid] and target < nums[j]:
                    i = mid+1
                else:
                    j = mid-1
        return -1