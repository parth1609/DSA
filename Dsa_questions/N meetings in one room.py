class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        count = 0
        last= 0
        meeting = [(start[i],end[i]) for i in range(n)]
        meeting.sort(key = lambda x:x[1])
        for S,E in meeting:
            if S > last:
                last = E
                count += 1
        
        return count 
        
