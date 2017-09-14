# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 21:36:11 2017

@author: zhangweiguo
"""
import numpy

# 输入输出均为二维数组
class Linear_Svm_Regression:
    def __init__(self, C):
        self.basic = lambda x,y:numpy.dot(x,y)
        self.C = C
    def Train(self,Data,Target):
        self.Dimsion_x = len(Data[0])
        self.Dimsion_y = len(Target[0])
        N = len(Data)
        self.kernel = Data
        self.Para = numpy.random.rand(N,self.Dimsion_y)


        batch_size = 100
        N_sample,N_dimsion = Data.shape
        E = 1e-4
        eta = 1e-2
        N_iteration = 1000
        e = self.Error(Data,Target)
        n = 0

        for j in range(self.Dimsion_y):
            Para = self.Para[:,j].reshape((-1,1))
            for i in range(N_iteration):
                if e < E:
                    break
                begin = batch_size * n % N_sample
                end = min(N_sample, begin + batch_size)
                data = Data[begin:end,:]
                target = Target[begin:end,j].reshape((-1,1))

                target_ = numpy.dot(self.basic(data, self.kernel.T),Para)
                Para_grad = self.C * Para * 2 / N + 2.0 / batch_size * \
                                                numpy.dot(self.basic(self.kernel, data.T), target_ - target)
                Para -= Para_grad*eta

                e= numpy.mean(numpy.square(target - target_)) + numpy.mean(numpy.square(Para)) * self.C
                print (i,e)
        self.Para[:,j] = Para.reshape((-1,))




    def Predict(self,Data):
        Y = numpy.dot(self.basic(Data, self.kernel.T),self.Para)
        return Y
    def Error(self,Data,Target):
        E1 = numpy.mean(numpy.square(self.Para)) * self.C
        E2 = numpy.mean(numpy.square(Target - self.Predict(Data)))
        E = E1 + E2
        return E



def test():
    Data = numpy.random.rand(3000, 3)
    Target1 = numpy.sum(Data, axis=1) + 3.0
    Target1 = Target1.reshape((-1,1))
    Target2 = 2*numpy.sum(Data, axis=1) + 2.0
    Target2 = Target2.reshape((-1,1))
    Target = numpy.hstack((Target1,Target2))
    L = Linear_Svm_Regression(1)
    L.Train(Data, Target)
    Score = L.Error(Data, Target)
    print L.Para
    print Score
    print Target - L.Predict(Data)


if __name__ == "__main__":
    test()