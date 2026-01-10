class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        # sol 1: str conversion
        # cnt = 0
        # for i in nums:
        #     s = str(i)
        #     if len(s) % 2 == 0:
        #         cnt += 1
        # return cnt

        # sol 2:
        cnt = 0
        for i in nums:
            if self.cntDigits(i) % 2 == 0:
                cnt += 1
        return cnt

    def cntDigits(self, i):
        cnt = 0
        while i > 0:
            i = i // 10
            cnt += 1
        return cnt