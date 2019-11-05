# ------------------------------
# 721. Accounts Merge
# 
# Description:
# Given a list accounts, each element accounts[i] is a list of strings, where the first 
# element accounts[i][0] is a name, and the rest of the elements are emails representing 
# emails of the account.
# 
# Now, we would like to merge these accounts. Two accounts definitely belong to the same 
# person if there is some email that is common to both accounts. Note that even if two 
# accounts have the same name, they may belong to different people as people could have 
# the same name. A person can have any number of accounts initially, but all of their 
# accounts definitely have the same name.
# 
# After merging the accounts, return the accounts in the following format: the first 
# element of each account is the name, and the rest of the elements are emails in sorted 
# order. The accounts themselves can be returned in any order.
# 
# Example 1:
# Input: 
# accounts = [["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], 
# ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
# Output: [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  
# ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
# 
# Explanation: 
# The first and third John's are the same person as they have the common email "johnsmith@mail.com".
# The second John and Mary are different people as none of their email addresses are used by other accounts.
# We could return these lists in any order, for example the answer [['Mary', 'mary@mail.com'], ['John', 'johnnybravo@mail.com'], 
# ['John', 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com']] would still be accepted.
# 
# Note:
# 
# The length of accounts will be in the range [1, 1000].
# The length of accounts[i] will be in the range [1, 10].
# The length of accounts[i][j] will be in the range [1, 30].
# 
# Version: 1.0
# 11/04/19 by Jianfa
# ------------------------------

class DSU:
    def __init__(self):
        self.p = [i for i in range(10001)] # [0, 1, ..., 10000]
    
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
    
    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)
        
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dsu = DSU()
        owners = {} # dictionary {email: owner}
        ids = {}    # dictionary {email: id}
        i = 0
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                owners[email] = name
                if email not in ids:
                    # grant an id to email if it's not shown before
                    ids[email] = i
                    i += 1
                dsu.union(ids[email], ids[acc[1]]) # union id of email and id of first email of this account
        
        ans = collections.defaultdict(list)
        for email in owners:
            ans[dsu.find(ids[email])].append(email)
        
        return [[owners[v[0]]] + sorted(v) for v in ans.values()]

# Used for testing
if __name__ == "__main__":
    test = Solution()

# ------------------------------
# Summary:
# Union Find solution from https://leetcode.com/problems/accounts-merge/solution/
# https://leetcode.com/problems/accounts-merge/discuss/109157/JavaC%2B%2B-Union-Find is
# also a good explanation.
# 
# O(A * logA) time where A = sum(a_i), a_i = len(accounts[i])
# O(A) space