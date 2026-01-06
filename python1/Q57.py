# nums = [1, 3, 5, 7]

# for nums1 in nums:
#     for nums2 in nums:
#         print('({}, {})'.format(nums1, nums2))

array = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

sum = 0
for i in array:
    for j in i:
        sum += j
print(sum)