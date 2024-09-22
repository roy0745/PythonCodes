class Test:
    def sum(self, nums: list[int], target: int) -> list[int]:
        n = len(nums)
        for i in range (n-1):
            for j in range (i+1, n):
                if nums[i] + nums[j] == target:
                    return (i, j)

        return()

a = Test()
print(a.sum(nums= [1,4,5,9],target=11))