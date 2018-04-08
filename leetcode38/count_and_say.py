class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n==0:
            return ''
        if n==1:
            return '1'
        list='1'
        for i in range(2,n+1):
            number=1
            perlist=list+'e'  #加入一个结束标记符
            list=''
            for j in range(len(perlist)-1):
                if perlist[j]==perlist[j+1] and perlist[j+1]!='e':
                    number+=1
                    char=perlist[j]
                elif perlist[j]!=perlist[j+1] and perlist[j+1]!='e':
                    char=perlist[j]
                    list=list+str(number)+char
                    char=perlist[j+1]
                    number=1
                elif perlist[j+1]=='e':
                    char=perlist[j]
                    list=list+str(number)+char
        return list