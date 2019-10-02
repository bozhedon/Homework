def get_two_sum(nums, k):
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if int(nums[i]) + int(nums[j]) == k:
                return [i, j]
    return None


if __name__ == '__main__':
    Nums = input('nums = ').split()
    K = int(input('k = '))
    print(get_two_sum(Nums, K))
