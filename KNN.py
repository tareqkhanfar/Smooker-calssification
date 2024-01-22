from sklearn.metrics import accuracy_score, classification_report
from sklearn.neighbors import KNeighborsClassifier
from main import Main


object = Main()
x_train=object.x_train
x_test=object.x_test
y_train=object.y_train
y_test=object.y_test
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit (x_train , y_train)
y_pred = knn.predict(x_test)
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Store the results
model = {'accuracy': accuracy, 'report': report}

print(model)
