from typing import List
def twoSum(nums: List[int], target: int) -> List[int]:
    # Your Codes
    ### Do not use input() or print() in your function## 
    # Inputs (nums, target) will given as arguments and the output as # 
    # ###return value
    for i,a in enumerate(nums):
        for k in range(i + 1, len(nums)):
            b = nums[k]
            if(a+b==target):
                return [i,k]
    return []
 