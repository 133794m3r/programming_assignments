class Solution:

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def tobst(nums,lo,hi):
            if lo > hi:
                return
            m = (lo+hi) >> 1
            root = TreeNode(nums[m])
            root.left = tobst(nums,lo,m-1)
            root.right = tobst(nums,m+1,hi)
            return root

        return tobst(nums,0,len(nums)-1)
