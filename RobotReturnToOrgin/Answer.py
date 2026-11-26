class Solution(object):
    def judgeCircle(self, moves):
        y=0
        z=0
        x=list(moves)
        for i in range(len(x)):
            if(x[i]=='U'):
                y+=1
            elif(x[i]=='R'):
                z+=2
            elif(x[i]=='D'):
                y+=-1
            elif(x[i]=='L'):    
                z+=-2
        if(y==0 and z==0):
            return True
        else:
            return False 
