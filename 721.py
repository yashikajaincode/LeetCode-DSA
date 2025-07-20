from typing import List
from collections import defaultdict

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        parent = {}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            parent[find(x)] = find(y)
        
        email_to_name = {}
        
        for account in accounts:
            name = account[0]
            for email in account[1:]:
                if email not in parent:
                    parent[email] = email
                union(account[1], email)
                email_to_name[email] = name
        
        groups = defaultdict(list)
        for email in parent:
            groups[find(email)].append(email)
        
        result = []
        for root_email, emails in groups.items():
            result.append([email_to_name[root_email]] + sorted(emails))
        
        return result
