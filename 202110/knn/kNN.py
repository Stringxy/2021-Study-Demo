import operator

from numpy import *


def creatDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    # tile函数把inX复制扩充为与dataSet对应大小的矩阵
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


def file2matrix(filename):
    fr = open(filename)
    arrayLines = fr.readlines()
    numberOfLines = len((arrayLines))
    returnMat = zeros((numberOfLines, 3))
    classLabelVector = []
    index = 0
    for line in arrayLines:
        line = line.strip()
        listFromLine = line.split(',')
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector


# 归一化特征值
def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    # normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet / tile(ranges, (m, 1))
    return normDataSet, ranges, minVals


# 测试分类效果
def dataClassTest(fileName):
    hoRatio = 0.10
    dataMat, dataLabels = file2matrix(fileName)
    normMat, ranges, minVals = autoNorm(dataMat)
    m = normMat.shape[0]
    numTestVecs = int(m * hoRatio)
    errorCount = 0
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i, :]
                                     , normMat[numTestVecs:m, :]
                                     , dataLabels[numTestVecs:m], 3)
        print('classifierResult:', classifierResult, '\nreal result:', dataLabels[i])
        if (classifierResult > dataLabels[i] + 3) | (classifierResult < dataLabels[i] - 3):
            errorCount += 1
    print('total error rate:', errorCount / numTestVecs)


def classifyPerson():
    age = int(input('your age:'))
    weight = int(input('your weight:'))
    height = int(input('your height:'))
    dataMat, dataLabels = file2matrix('knn/testSet.txt')
    normMat, ranges, minVals = autoNorm(dataMat)
    inX = array([age, weight, height])
    result = classify0((inX - minVals) / ranges, normMat, dataLabels, 3)
    print('score:', result)
