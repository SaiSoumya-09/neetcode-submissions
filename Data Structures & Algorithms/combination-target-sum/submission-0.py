class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        def backt(start,current,total):
            if total==target:
                result.append(current[:])
                return 
            
            if total>target:
                return 
            
            for i in range(start,len(nums)):
                current.append(nums[i])
                backt(i,current,total+nums[i])
                current.pop()
        backt(0,[],0)
        return result