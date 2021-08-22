from typing import *

'''二分查找'''
def search(nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2          
            if nums[pivot] == target:
                print()
                info = "目标索引：" + str(pivot)
                print(info)
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1

Nums = [-1,0,3,5,9,12]
Target = 9          
search(nums = Nums,target = Target)





