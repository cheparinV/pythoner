import pandas as pd
import numpy as np
import operator
from sklearn import datasets
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold

boston = datasets.load_boston()
data = pd.DataFrame(boston.data, columns=boston.feature_names)
pre_proc = preprocessing.scale(data)
res = []
res_p = []
for i in np.linspace(1, 10, num=200):
    kf = KFold(n_splits=5, shuffle=True, random_state=42)
    kn = KNeighborsRegressor(n_neighbors=5, weights='distance', metric='minkowski', p=i)
    res_p.append(i)
    res.append(
        np.mean(cross_val_score(estimator=kn, cv=kf, X=pre_proc, y=boston.target, scoring='neg_mean_squared_error')))

index, value = max(enumerate(res), key=operator.itemgetter(1))
print res_p[index]
