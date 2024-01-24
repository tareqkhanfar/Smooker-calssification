from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
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

# Generate a classification report
report = classification_report(y_test, y_pred)

# Generate a confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)

# Store the results in a dictionary
model_results = {
    'accuracy': accuracy,
    'classification_report': report,
    'confusion_matrix': conf_matrix
}

# Print the model's results
print(f"Accuracy: {model_results['accuracy']}")
print(f"Classification Report:\n{model_results['classification_report']}")
print(f"Confusion Matrix:\n{model_results['confusion_matrix']}")