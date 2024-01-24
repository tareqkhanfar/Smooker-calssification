from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score, roc_auc_score

from main import Main


object = Main()
x_train = object.x_train
y_train = object.y_train
x_test = object.x_test
y_test = object.y_test
import seaborn as sns
import matplotlib.pyplot as plt


nb_classifier = GaussianNB()
nb_classifier.fit(x_train, y_train)
y_pred = nb_classifier.predict(x_test)
conf_matrix = confusion_matrix(y_test, y_pred)

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)
roc_auc = roc_auc_score(y_test, nb_classifier.predict_proba(x_test)[:, 1])

# Print the model's results
print(f"Accuracy: {accuracy}")
print(f"precision: {precision}")

print(f"recall: {recall}")

print(f"f1: {f1}")
print(f"roc_auc: {roc_auc}")



sns.heatmap(conf_matrix, annot=True, fmt='g', cmap='Blues', cbar=False)
plt.title('Confusion Matrix')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.show()