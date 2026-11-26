class Solution(object):
    def canAliceWin(self, nums):
        x=[]
        y=[]
        for i in range(len(nums)):
            if(nums[i]/2>=5):
                x.append(nums[i])
            else:
                y.append(nums[i])
        if(sum(x)>sum(y) or sum(x)<sum(y)):
            return True
        else:
            return False