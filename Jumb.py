class solution:
    def canJump(self, nums:list[int]) -> bool:
        gas=0
        for i in nums:
            if gas<0:
                return False
            elif i>gas:
                gas=i
            gas-=1
        return True
