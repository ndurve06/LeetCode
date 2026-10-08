class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        string_array = []
        for i in range(len(nums)):
            string_array.append(str(nums[i]))
        string_array.sort(key=lambda x: x*10, reverse=True)

        if string_array[0] == "0":
            return "0" 

        return "".join(string_array)

testing = Solution()
print(testing.largestNumber([10,2]))
print(testing.largestNumber([3,30,34,5,9]))

#runtime: 0ms, beats 100%
#memory: 19.43MB, beats 7.16%