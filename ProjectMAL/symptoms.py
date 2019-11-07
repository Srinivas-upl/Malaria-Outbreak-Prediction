import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


balance_data = pd.read_csv('ab.csv')
X = balance_data.values[:, 1:5]
Y = balance_data.values[:,0]


X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.3, random_state = 100)

clf_gini = DecisionTreeClassifier(criterion = "gini", random_state = 100,
                               max_depth=3, min_samples_leaf=5)
clf_gini.fit(X_train, y_train)
clf_entropy = DecisionTreeClassifier(criterion = "entropy", random_state = 100,
 max_depth=3, min_samples_leaf=5)
clf_entropy.fit(X_train, y_train)

y_pred = clf_gini.predict(X_test)
y_pred
X_train=X_train[:,0]
plt.scatter(X_train,y_train,color = 'red')
plt.plot(X_train,clf_gini.predict(X_train),color='blue')
plt.show()
X_test=X_test[:,0]
plt.scatter(X_test,y_test,color='red')
plt.plot(X_train,clf_gini.predict(X_train),color='blue')
plt.show()
from sklearn.metrics import accuracy_score
print('Accuracy Score on train data: ', accuracy_score(y_true=y_train, y_pred=clf_gini.predict(X_train)))
print('Accuracy Score on the test data: ', accuracy_score(y_true=y_test, y_pred=clf_gini.predict(X_test)))