def containsDuplicate(nums: list[int]) -> bool:
    hashset = set()

    for n in nums:
        if n in hashset:
            return True
        hashset.add(n)
    return False

print(containsDuplicate([1,2,3,4,1,5]))
print(containsDuplicate([1,2,3,4,5]))