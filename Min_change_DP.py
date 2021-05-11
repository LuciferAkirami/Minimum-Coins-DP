"""
@author: Lucifer Akirami
"""
#recursive solution
arr = [1,3,5]
n = 15

def rec(n,arr):
    if n < 0: return n+1
    if n == 0: return 0
    ans = n+1
    for i in arr:
        if n-i>=0:
            ans = min(ans,1+rec(n-i,arr))
    return ans

print(rec(n,arr))

#dynamic  memoization

def rec_dp(n,arr,dp={}):
    if n < 0: return n+1
    if n == 0: return 0
    if n in dp.keys(): return dp[n]
    ans = n+1
    for i in arr:
        if n-i>=0:
            ans = min(ans,1+rec_dp(n-i,arr,dp))
            dp[n] = ans
    return ans

print(rec_dp(24,[1,7,3]))
