from typing import List,Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        return Solution.recursive(self, nums=nums, left=0, right=len(nums) - 1)
        
    def recursive(self, nums:List[int], left: int, right: int):
        if left > right:
            return None
        
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = Solution.recursive(self, nums, left, mid - 1)
        root.right = Solution.recursive(self, nums, mid + 1, right)
        return root