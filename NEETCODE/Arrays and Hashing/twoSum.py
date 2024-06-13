def twoSum(nums:list[int],target:int) -> bool:
    prevMap = {}

    for i, n in enumerate(nums):
        diff = target - n
        if diff in prevMap:
            return [prevMap[diff],i]
        prevMap[n] = i
    return

print(twoSum([1,2,3],3))