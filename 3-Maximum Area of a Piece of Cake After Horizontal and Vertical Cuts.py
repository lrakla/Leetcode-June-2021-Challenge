class Solution:
    def horizontal(hc,h,horizontalCuts):
        if hc==1:
            a = h-horizontalCuts[0]
            hor_diff = max(a,horizontalCuts[0])
        else :
            horizontalCuts.sort()
            hor_diff = 0
            for i in range(hc-1):
                curr_diff = horizontalCuts[i+1]-horizontalCuts[i]
                hor_diff = max(hor_diff,curr_diff)
                
        return max(hor_diff, h-horizontalCuts[hc-1],horizontalCuts[0])
        
    def vertical(vc,w,verticalCuts):
        if vc==1:
            a = w-verticalCuts[0]
            ver_diff = max(a,verticalCuts[0])
        else :
            verticalCuts.sort()
            ver_diff = 0
            for i in range(vc-1):
                curr_diff = verticalCuts[i+1]-verticalCuts[i]
                ver_diff = max(ver_diff,curr_diff)
        return max(ver_diff,w -verticalCuts[vc-1],verticalCuts[0])
   
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        hc = len(horizontalCuts)
        vc = len(verticalCuts)
        hor_diff = Solution.horizontal(hc,h,horizontalCuts)
        ver_diff = Solution.vertical(vc,w,verticalCuts)
        return hor_diff*ver_diff % (pow(10,9)+7)
        
        