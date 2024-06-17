# Check If two Line segments Intersect

#User function Template for python3

class Solution:
    def orientation(self,p,q,r):
        '''
        0 -> collinear 
        1 -> clockwise
        2 -> countrclockwise / anticlockwise
        '''
        val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
        if val == 0:
            return 0
        elif val > 0:
            return 1
        else:
            return 2
            
    def onsegment(self,p,q,r):
        # to check if point of second line lies on first line or not 
        if min(p[0],r[0]) <= q[0] <= max(p[0],q[0]) and min(p[1],r[1]) <= q[1] <= max(p[1],q[1]):
            return True
        return False 
       
    def doIntersect(self, p1, q1, p2, q2):
        #code here
        
        o1 = self.orientation(p1,q1,p2)
        o2 = self.orientation(p1,q1,q2)
        o3 = self.orientation(p2,q2,p1)
        o4 = self.orientation(p2,q2,q1)
        
        # general case when the lines are intersect
        if o1 != o2 and o3!= o4:
            return "true"
            
        # special cases
        if o2 == 0 and self.onsegment(p1,p2,q1):
            return "true"
        
        if o2 == 0 and self.onsegment(p1,q2,q1):
            return "true"
        
        if o2 == 0 and self.onsegment(p2,p1,q2):
            return "true"
        
        if o2 == 0 and self.onsegment(p2,q2,q2):
            return "true"
        
        return "false"
        
        
        
        
