class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = max_sum = nums[0]
        
        for num in nums [1:]:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)

        return max_sum
 
#->Kadane’s Algorithm
#Kadane’s Algorithm is a famous and efficient algorithm used to solve the Maximum Subarray Problem
#that is, to find the contiguous subarray with the maximum sum within a one-dimensional array of numbers.
    ## num[]   curr_sum     max_sum
    ## curr_sum = max_sum = nums[0] = -2
    ## loop starts from num[1]:
    ##  1       max(1,-1)   max(-2,1)
    ##  -3      max(-3,-2)  max(1,-2)
    ##  4       max(4,2)    max(1,4)
    ##  -1      max(-1,3)   max(3,4)
    ##  2       max(2,5)    max(4,5)
    ##  1       max(1,6)    max(5,6)
    ##  -5      max(-5,1)   max(6,1)
    ##  4       max(4,5)    max(6,5)
