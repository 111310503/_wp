def most_common(nums):
    count = {}
    for num in nums:
        count[num] = count.get(num, 0) + 1
    return max(count, key=count.get)
nums = [1, 2, 2, 3, 3, 3, 4]
print(most_common
