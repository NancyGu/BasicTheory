# demo1:
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import cross_val_score
from sklearn import datasets
iris = datasets.load_iris()
gnb = GaussianNB()
scores = cross_val_score(gnb,iris.data,iris.target,cv=10)
#print("Accuacy:%.5f"%scores.mean())

# demo2:
# kaggle : San Francisco criminal classification
# Path E:\data\kangle
import pandas as pd
import numpy as np
from sklearn import preprocessing
from sklearn.metrics import log_loss
from sklearn.cross_validation import train_test_split
train = pd.read_csv("E:\data\kangle//train_data.csv",parse_dates=['Dates'])
test = pd.read_csv("E:\data\kangle//test_data.csv",parse_dates=['Dates'])

# step1: preprocessing -------------------------------------------------------------------------------------------------
# sklearn.preprocessing LableEncoder 对类别做编号
# pandas get_dummies() 二值化01向量
# 1.1 对犯罪类别Category，用LableEncoder做编号
#对犯罪类别:Category; 用LabelEncoder进行编号
leCrime = preprocessing.LabelEncoder()
crime = leCrime.fit_transform(train.Category)   #39种犯罪类型
#用get_dummies因子化星期几、街区、小时等特征
days=pd.get_dummies(train.DayOfWeek)
district = pd.get_dummies(train.PdDistrict)
hour = train.Dates.dt.hour
hour = pd.get_dummies(hour)
#组合特征
trainData = pd.concat([hour, days, district], axis = 1)  #将特征进行横向组合
trainData['crime'] = crime   #追加'crime'列
days = pd.get_dummies(test.DayOfWeek)
district = pd.get_dummies(test.PdDistrict)
hour = test.Dates.dt.hour
hour = pd.get_dummies(hour)
testData = pd.concat([hour, days, district], axis=1)

trainData

#Step 2: Create Model---------------------------------------------------------------------------------------------------
from sklearn.naive_bayes import BernoulliNB
import time
features=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', 'BAYVIEW', 'CENTRAL', 'INGLESIDE', 'MISSION',
 'NORTHERN', 'PARK', 'RICHMOND', 'SOUTHERN', 'TARAVAL', 'TENDERLOIN']
X_train, X_test, y_train, y_test = train_test_split(trainData[features], trainData['crime'], train_size=0.6)
NB = BernoulliNB()
nbStart = time.time()
NB.fit(X_train, y_train)
nbCostTime = time.time() - nbStart
#print(X_test.shape)
propa = NB.predict_proba(X_test)
#X_test为263415*17； 那么该行就是将263415分到39种犯罪类型中，每个样本被分到每一种的概率
print("朴素贝叶斯建模%.2f秒"%(nbCostTime))
predicted = np.array(propa)
logLoss=log_loss(y_test, predicted)
print("朴素贝叶斯的log损失为:%.6f"%logLoss)