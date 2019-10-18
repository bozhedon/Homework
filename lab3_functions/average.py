def average(*nums):
    avg = 0
    for n in nums:
        avg = avg + n
    if avg != 0:
        return avg / len(nums)
    return None


print(average())  # => None
print(average(5))  # => 5.0
print(average(6, 8, 9, 11))  # => 8.5

l = [3, 1, 41, 592, 65358]  # or any other user-defined input.
print(average(l))