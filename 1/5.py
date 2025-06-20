def sieve(nums):
  uni_nums = set(nums)
  uni_nums = sorted(uni_nums, reverse=True)
  result = tuple(uni_nums)
  return result
nums = [1,3,4,5,3,2,5,6,9]
print(sieve(nums))
