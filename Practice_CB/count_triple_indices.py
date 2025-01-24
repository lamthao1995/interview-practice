"""
Problem Description

You are given three sorted arrays A, B, and C, each of size n, and an integer D. The task is to count the number of unique tuples (i, j, k) where:

i is an index in array A,
j is an index in array B,
k is an index in array C,
such that the following conditions are satisfied:

|A[i] - B[j]| ≤ D,  |A[i] - C[k]| ≤ D,  |B[j] - C[k]| ≤ D
Input

A, B, C: Lists of integers of length n, sorted in non-decreasing order.
D: An integer representing the maximum allowable absolute difference.
"""

class CountTriple:
    def __init__(self):
        pass
    def get_count(self, nums1, nums2, nums3, d)->int:
        ans = 0
        idx2 = idx3 = 0

        for val in nums1:
            idx2 = self.get_next_element(nums2, idx2, val - d)
            idx3 = self.get_next_element(nums3, idx3, val - d)

            idx2_end = self.get_next_element(nums2, idx2, val + d + 1)
            idx3_end = self.get_next_element(nums3, idx3, val + d + 1)



    def get_count_with_fix_min(self, nums_min, nums2, nums3, d):
        ans = 0
        for val in nums_min:

