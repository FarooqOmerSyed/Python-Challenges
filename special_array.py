def special_array(nums: list):
    def parity(n):
        if n % 2 == 1:
            return 'odd'
        else:
            return 'even'

    for i in range(1,len(nums)):
        if parity(nums[i]) == parity(nums[i-1]):
            return False

    return True


print(special_array([4, 3, 1, 6]))
