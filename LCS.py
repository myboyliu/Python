import numpy



'''
LCS 最大公共子序列
LCCS 最大公共子串
Manacher 最长回文子串
'''


class CS:
    def __init__(self):
        pass
    @staticmethod
    def LCS(s1,s2):
        N1 = len(s1)
        N2 = len(s2)
        Len = numpy.zeros((N1+1, N2+1))
        Dire = numpy.zeros((N1+1, N2+1))
        if N1 == 0 or N2 == 0:
            max_len = 0
            max_str = ""
        else:
            for i in range(1,N1+1):
                for j in range(1,N2+1):
                    if s1[i-1] == s2[j-1]:
                        Len[i,j] = Len[i-1,j-1] + 1
                        Dire[i,j] = 1
                    else:
                        a1 = Len[i-1,j]
                        b1 = Len[i,j-1]
                        if a1>b1:
                            Len[i,j] = a1
                            Dire[i,j] = 2
                        else:
                            Len[i,j] = b1
                            Dire[i,j] = 3
        max_len = int(Len[N1, N2])
        S = ""
        while N1>=1 and N2 >=1 :
            if Dire[N1, N2] == 1:
                S = s1[N1-1] + S
                N1 -= 1
                N2 -= 1
            elif Dire[N1, N2] == 2:
                N1 -= 1
            elif Dire[N1, N2] == 3:
                N2 -= 1
        max_str = S
        return max_len, max_str

    @staticmethod
    def LCCS(s1,s2):
        max_len = 0
        max_str = ""
        last_locate = 0
        N1 = len(s1)
        N2 = len(s2)
        Len = numpy.zeros((N1+1, N2+1))
        if N1 == 0 or N2 == 0:
            return max_len,max_str
        else:
            for i in range(1,N1+1):
                for j in range(1,N2+1):
                    if s1[i-1] == s2[j-1]:
                        Len[i,j] = Len[i-1,j-1] + 1
                        if max_len < Len[i,j]:
                            max_len = Len[i,j]
                            last_locate = i-1
                    else:
                        Len[i,j] = 0
            max_len = int(max_len)
            last_locate += 1
            max_str = s1[last_locate-max_len:last_locate]
            return max_len, max_str
    @staticmethod
    def Manacher(s1):
        pass

    @staticmethod
    def Kmp():
        pass

s1 = "abdcdfgggvt"
s2 = "dgfabcdcdfg"
# s1 = "zhangweiguo"
# s2 = "wozhangsan"
print CS.LCCS(s1,s2)