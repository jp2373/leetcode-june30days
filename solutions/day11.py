class Solution:
    def sortColors(self, nums: List[int]) -> None:
        begin = 0
        middle = 0
        end = len(nums) - 1
        
        while middle <= end:
            if nums[middle] == 0:
                nums[begin], nums[middle] = nums[middle], nums[begin]
                middle += 1
                begin += 1
            elif nums[middle] == 2:
                nums[middle], nums[end] = nums[end], nums[middle]
                end -= 1
            else:  #nums[mid] == 1:
                middle += 1
        
