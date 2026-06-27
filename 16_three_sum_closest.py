class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        result = nums[0] + nums[1] + nums[2]
        
        for i in range (len(nums) - 2):
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total == target:
                    return total
                
                if abs(total - target) < abs(result - target):
                    result = total
                
                if total < target:
                    j = j + 1
                elif total > target:
                    k = k - 1

        return result 
    
#runtime: 404ms, beats 22.91%
#memory: 19.18MB, beats 96.18%