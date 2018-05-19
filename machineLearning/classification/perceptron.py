# 感知机

import numpy as np


class Perceptron():
    def __init__(self):
        self._w = None
        self._b = None
    def fit(self, x,y ,learning_rate = 0.1, epoch = 1000):
        # epoch: the upper limit of gradient
        x,y = np.asarray(x,np.float32),np.asarray(y,np.float32)
        self._w = np.zeros(x.shape[1])
        self._b = 0

        for __ in range(epoch):
            # cal w*x + b
            y_pred = x.dot(self._w) + self._b
            # argmax funciton in numpy:
            #     return the max point in y
            idx = np.argmax(np.maximum(0,-y_pred*y))
            # if y_pred * yi < 0 mis-classified point
            if y[idx] * y_pred[idx] > 0:
                break
            delta = learning_rate * y[idx]
            self._w = self._w + delta * x[idx]
            self._b = self._b + delta
            print(__,self._w,self._b)
            #print("f(x) = %.5f * x + %.5f"%(self._w,self._b))

    def predict(self, x, raw = False):
        x = np.asarray(x, np.float32)
        y_pred = x.dot(self._w) + self._b
        if raw:
            return y_pred
        return np.sign(y_pred).astype(np.float32)

from Util import gen_two_clusters

x, y = gen_two_clusters()
perceptron = Perceptron()
perceptron.fit(x, y)
print("准确率：{:8.6} %".format((perceptron.predict(x) == y).mean() * 100))


from Util import visualize2d

visualize2d(perceptron, x, y)
visualize2d(perceptron, x, y, True)
#if __name__ == '__main__':
    #x = [[3,3],[4,3],[1,1]]
    #y = [1,1,-1]

    #inis = Perceptron()
    #inis.fit(x,y)


