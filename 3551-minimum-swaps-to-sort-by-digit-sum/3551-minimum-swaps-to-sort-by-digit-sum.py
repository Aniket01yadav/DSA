class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        def get_digit_sum(x: int) -> int:
            s = 0
            while x > 0:
                s += x % 10
                x //= 10
            return s

        n = len(nums)

        arr = []
        for i in range(len(nums)):
            val = nums[i]
            digit_sum = get_digit_sum(val)
            arr.append((digit_sum, val, i))

        arr.sort()
        visited = [False] * n
        swaps = 0

        for i in range(n):
            if visited[i] or arr[i][2] == i:
                continue

            cycle_size = 0
            curr = i
            while not visited[curr]:
                visited[curr] = True
                curr = arr[curr][2]
                cycle_size += 1

            if cycle_size > 1:
                swaps += cycle_size - 1

        return swaps