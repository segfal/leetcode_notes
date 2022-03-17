
def twoSum(nums: List[int], target: int) -> List[int]:
        '''
            an array of integers
            target
            two nums add to target
            
            so something like target = nums[i] + nums[j]
            
            one solution
            we should not have any duplicates
            
            
            target -nums[i] = nums[j]
            
            
            Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].


            9-7 = 2
            
            key : value
            2       0
            7       1
        '''
        
        
        table = {}
        
        for i in range(len(nums)):
            if target - nums[i] not in table:
                table[nums[i]] = i
            else:
                j = table[target - nums[i]]
                return [i,j]
            
        return []
