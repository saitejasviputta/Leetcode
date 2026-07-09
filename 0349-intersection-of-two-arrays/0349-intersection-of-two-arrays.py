class Solution(object):
    def intersection(self, nums1, nums2):
        n=len(nums1)
        res=[]
        for i in range (0,n):
            if nums1[i] in nums2:
                res.append(nums1[i])
        r=set(res)
        f=list(r)
        return f