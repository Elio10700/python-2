class pairofelements:
    def twosum(self, nums, target):
        sum = 0
        lookup = {}
        for i, num in enumerate(nums):
            sum = sum + num
            if sum >= target:
                print("The index value is", i)
                lookup[i] = sum
                print(lookup)
                return
            lookup[i] = sum


p1 = pairofelements()
p1.twosum((10, 20, 20, 30, 40, 100), 70)
