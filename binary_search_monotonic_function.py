# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 0
        high = n
        ans = 0
        while low <= high:
            mid = low + (high - low)//2
            if isBadVersion(mid):
                # ans = mid
                high = mid - 1
            if not isBadVersion(mid):
                ans = mid
                low =  mid + 1
        return ans+1
