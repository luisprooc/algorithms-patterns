# def missing_numbers(arr):
#   i = 0
#   while i < len(arr):
#     j = arr[i] - 1
#     if arr[i] != arr[j]:
#       arr[i], arr[j] = arr[j], arr[i]  # swap
#     else:
#       i += 1

#   missing = []

#   for i in range(len(arr)):
    
#     if arr[i] != i + 1:
#       missing.append(i + 1)

#   return missing

def find_corrupt_numbers(nums):
  i = 0

  while i < len(nums):
    j = nums[i] - 1
    if nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]
    
    else:
      i += 1
  

  corrupts = [-1, -1]

  pt1, pt2 = 0, len(nums) -1
  while pt1 < len(nums) // 2:
    if nums[pt1] != pt1 + 1:
      corrupts[1] = pt1 + 1
    
    elif nums[pt2] != pt2 + 1:
      corrupts[1] = pt2 + 1

    if nums.count(nums[pt1]) > 1:
      corrupts[0] = nums[pt1]

    elif nums.count(nums[pt2]) > 1:
      corrupts[0] = nums[pt2]

    
    pt1,pt2 = pt1 + 1, pt2 -1

  return corrupts 


def main():
  arr = [int(i) for i in input().split()]
  print(find_corrupt_numbers(arr))


main()