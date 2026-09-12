class Solution:

  def maximumWeight(self, intervals: list[list[int]]) -> list[int]:
    arr = []
    for i, (l, r, weight) in enumerate(intervals):
      arr.append((r, l, weight, i))
    arr.sort()

    n = len(arr)
    rights = [item[0] for item in arr]

    def find_first_ge(target: int) -> int:
      low, high = 0, n
      while low < high:
        mid = (low + high) // 2
        if rights[mid] >= target:
          high = mid
        else:
          low = mid + 1
      return low

    dp = [[(0, ())] * (n + 1) for _ in range(5)]

    for i in range(1, n + 1):
      r, l, weight, orig_idx = arr[i - 1]
      prev_j = find_first_ge(l)

      for k in range(1, 5):
        best_score, best_indices = dp[k][i - 1]

        prev_score, prev_indices = dp[k - 1][prev_j]
        new_score = prev_score + weight

        new_indices = sorted(prev_indices + (orig_idx,))
        new_indices = tuple(new_indices)

        if new_score > best_score:
          best_score, best_indices = new_score, new_indices
        elif new_score == best_score:
          if not best_indices or new_indices < best_indices:
            best_indices = new_indices

        dp[k][i] = (best_score, best_indices)

    best_score = -1
    best_ans = ()

    for k in range(1, 5):
      score, indices = dp[k][n]
      if score > best_score:
        best_score = score
        best_ans = indices
      elif score == best_score:
        if not best_ans or indices < best_ans:
          best_ans = indices

    return list(best_ans)