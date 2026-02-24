def twoSum(nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return[i,j]
                
print(twoSum(nums = [9,4,1,2,3,4,5], target = 9) )
print(twoSum(nums = [8,3,2,1,3], target = 6))          
print(twoSum(nums = [4,2], target = 6))