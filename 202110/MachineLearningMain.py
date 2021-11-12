import matplotlib.pyplot as plt
import knn.kNN as kNN
import trees.trees as trees
from numpy import *
if __name__ == "__main__":
   # dataMat,dataLabel = kNN.file2matrix('knn/testSet.txt')
   # fig = plt.figure()
   # #把画布分成一行一列，并把该子图放在第一位
   # ax = fig.add_subplot(111)
   # ax.scatter(dataMat[:,1],dataMat[:,2],15.0*array(dataLabel),15.0*array(dataLabel),marker='o')
   # plt.show()
   # normMat,ranges,minVals =kNN.autoNorm(dataMat)
   # print('normMat:{}',normMat)
   # print('ranges:{}',ranges)
   # print('minVals:{}',minVals)
   #kNN.dataClassTest('knn/testSet.txt')
   # kNN.classifyPerson()
   myDat,labels = trees.createDataSet()
   # Ent = trees.calcShannonEnt(myDat)
   # print(Ent)
   # bestFeature = trees.chooseBestFeatureToSplit(myDat)
   # print(bestFeature)
   myTree = trees.createTree(myDat,labels)
   print(myTree)