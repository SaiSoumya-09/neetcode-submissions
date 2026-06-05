class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
            num=nums[i]
            rem=target-num
            if rem in seen:
                return [seen[rem],i]
            seen[num]=i
        