#Question 1
def is_palindrome(s):
    left = 0
    right = len(s)-1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

#Question 2
def has_pair_with_sum(nums, target):
    left = 0
    right = len(nums)-1
    while left < right:
        total = nums[left] + nums[right]
        if total < target:
            left += 1
        elif total > target:
            right -= 1
        else:
            return True
    return False

#Question 3
def reverse_list(nums):
    left = 0
    right = len(nums)-1
    while left < right:
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp
        left += 1
        right -= 1
    return nums

#Question 4
def is_palindrome_ignore_case(s):
    s = s.lower()
    left = 0
    right = len(s)-1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return False
    return True

#Question 5
def move_zeroes(nums):
    non_zeroes = [x for x in nums if x != 0]
    zeroes = [x for x in nums if x == 0]
    return non_zeroes + zeroes

if __name__ == "__main__":
    print("is_palindrome('racecar'):", is_palindrome("racecar"))
    print("has_pair_with_sum([1,2,3,4,5], 9):", has_pair_with_sum([1,2,3,4,5], 9))
    print("reverse_list([1,2,3,4,5]):", reverse_list([1,2,3,4,5]))
    print("is_palindrome_ignore_case('Racecar'):", is_palindrome_ignore_case("Racecar"))
    print("move_zeroes([0,1,0,3,12]):", move_zeroes([0,1,0,3,12]))