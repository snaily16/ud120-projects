#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

# ---------- K Nearset Neighbor ----------------
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

clf_knn = KNeighborsClassifier(n_neighbors=4)
clf_knn.fit(features_train, labels_train)
knn_pred=clf_knn.predict(features_test)
print "Accuracy kNN: ", accuracy_score(labels_test, knn_pred)

# ----------------Random Forest -------------------
from sklearn.ensemble import RandomForestClassifier

clf_rf = RandomForestClassifier(n_estimators=15, min_samples_split=10)
clf_rf.fit(features_train, labels_train)
rf_pred = clf_rf.predict(features_test)
print "Accuracy Random Forest: ", accuracy_score(labels_test, rf_pred)

# ---------------- Adaboost ------------------------
from sklearn.ensemble import AdaBoostClassifier
clf_ab = AdaBoostClassifier(n_estimators=100)
clf_ab.fit(features_train, labels_train)
ab_pred = clf_ab.predict(features_test)
print "Accuracy Adaboost: ", accuracy_score(labels_test, ab_pred)

try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
