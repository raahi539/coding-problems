nums = [1,2,3,4,5]
target = 9

def two_sum():
    for i in range(len(nums)):
        for c in range(len(nums)):
            if i != c and nums[i] + nums[c] == target:
                return i, c

print(two_sum())