class Solution:
    def merge_bst(self,root,result):
        if root:
            self.merge_bst(root.left,result)
            result.append(root.data)
            self.merge_bst(root.right,result)
            
            
    def merge(self, root1, root2):
        # code here
        arr1 = []
        arr2 = []
        self.merge_bst(root1,arr1)
        self.merge_bst(root2,arr2)
        
       
        merged = self.sort_merge_array(arr1,arr2)
        
        return merged
    
    def sort_merge_array(self,arr1,arr2):
        merged = []
        i = 0
        j = 0
        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                merged.append(arr1[i])
                i+=1
            else:
                merged.append(arr2[j])
                j+=1
        # remaining element in both array
        while i < len(arr1):
            merged.append(arr1[i])
            i+=1
        
        while j < len(arr2):
            merged.append(arr2[j])
            j+=1
        
        return merged
            
                
        
