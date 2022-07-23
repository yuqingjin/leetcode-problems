# Mehthod: DFS
# Time Complexity: 
    # N: num of account; K: max num of emails per user
    # graph traversal: time to traversal all emails: O(NK)
    # each time sort emaillist: perform sort N times and each time sort length K list: O(N*logK)
    # total: multiply them, O(N*K*N*logK)
    
# Space Complexity: dominate by graph, O(NK)

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # two dict：one for build graph, all the relations between emails in the given list
        # and another for keep name:email_list
        graph = defaultdict(set)
        email_to_name = {} # to avoid the sitation that different people have the same name
        
        # for graph: connect the rest of emails to the first email, 
        # and connect the first to the rest
        for account in accounts:
            name = account[0]
            for email in set(account[1:]):
                # print(set(account[1:]))
                graph[account[1]].add(email)
                graph[email].add(account[1])

                email_to_name[email] = name 
        # print("graph", graph)
        
        
        # build a set to avoid repeated visit
        res = [] # need to be sorted
        visited = set()
        stack = []
        
        
        # traverse emails in graph to merge those belonging to the same user together
        for email in graph:
            if email not in visited:
                visited.add(email)
                name = email_to_name[email]
                stack.append(email)
                local_res = []
                
                # do DFS
                # stack is for store the connected components
                while stack:
                    # print("stack", stack)
                    cur = stack.pop()
                    local_res.append(cur)
                    
                    # continue to go deep: find out their child and append to stack
                    for sub_email in graph[cur]:
                        if sub_email not in visited:
                            visited.add(sub_email)
                            stack.append(sub_email)
                            
                res.append([name] + sorted(local_res))
                
        return res
        
        
