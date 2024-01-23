from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

from main import Main


object = Main()
x_train = object.x_train
y_train = object.y_train
x_test = object.x_test
y_test = object.y_test


nb_classifier = GaussianNB()
nb_classifier.fit(x_train, y_train)
predictions = nb_classifier.predict(x_test)
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy}")