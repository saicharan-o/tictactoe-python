def twoSum(nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j]==target:
                    return[i,j]
                
print(twoSum(nums = [9,4,1,2,3,4,5], target = 9) )
print(twoSum(nums = [8,3,2,1,3], target = 6))          
print(twoSum(nums = [4,2], target = 6))

print(twoSum(nums = [9,4,1], target = 11) )
print(twoSum(nums = [8,3,2], target = 14))          
print(twoSum(nums = [1,1,2,2,2], target = 2))

print(twoSum(nums = [9,8,7,6,3,2], target = 12) )
print(twoSum(nums = [10,2,3,5,7,8,3], target = 87))          
print(twoSum(nums = [3,99,7,94,2,2], target = 49))

print(twoSum(nums = [94,4,6,7,3,2,8], target = 199) )
print(twoSum(nums = [9,9,1,2,3,4,5,6], target = 16))          
print(twoSum(nums = [7,6,4,2,3], target = 8))

print(twoSum(nums = [0,2,4,5,72,2,1,5], target = 39) )
print(twoSum(nums = [9,2,3,5,2,1,4], target = 14))          
print(twoSum(nums = [0,8,1,4,8,2], target = 10))

