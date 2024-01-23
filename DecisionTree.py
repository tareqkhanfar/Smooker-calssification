from sklearn.tree import DecisionTreeClassifier
from main import Main
from sklearn.metrics import accuracy_score


object = Main()
x_train = object.x_train
y_train = object.y_train
x_test = object.x_test
y_test = object.y_test

clf = DecisionTreeClassifier()
clf.fit(x_train, y_train)

# Predictions and evaluation
predictions = clf.predict(x_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy}")