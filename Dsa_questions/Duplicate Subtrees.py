class Solution:
    def printAllDups(self, root):
        ret = {}
        seen = set()
        
        def dfs(cur):
            if not cur:
                return "#"
            
     
            left = dfs(cur.left)
            right = dfs(cur.right)
            
            subtree_structure = "{},{},{}".format(cur.data, left, right)

            
            if subtree_structure in seen:
                if subtree_structure not in ret:
                    ret[subtree_structure] = cur
            else:
                seen.add(subtree_structure)
                
            return subtree_structure
        
        dfs(root)
        
        return list(ret.values())
