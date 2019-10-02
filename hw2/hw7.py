def get_two_sum(nums, t):
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            for k in range(j + 1, len(nums)):
                if int(nums[i]) + int(nums[j]) + int(nums[k]) == t:
                    return [i, j, k]
    return None


if __name__ == '__main__':
    Nums = input('nums = ').split()
    K = int(input('k = '))
    print(get_two_sum(Nums, K))
