class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        n = len(arr)
        sum_arr = sum(arr)
        if sum_arr % 3 != 0:
            return False
        target = sum_arr // 3
        curr_sum = 0
        partitions = 0
        for i in range(n):
            curr_sum += arr[i]
            if curr_sum == target:
                partitions += 1
                curr_sum = 0
                if partitions == 2 and i < len(arr) - 1:
                    return True
        return False