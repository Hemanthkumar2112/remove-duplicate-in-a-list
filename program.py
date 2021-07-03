    def removeDuplicates(self, nums:List[int]) -> int:
        nums.sort()
        for i in nums:
            while nums.count(i)>1:
                nums.remove(i)
        print(nums)
