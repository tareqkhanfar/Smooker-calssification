import tensorflow as tf
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score, roc_auc_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from main import Main
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
object = Main()
x_train=object.x_train
x_test=object.x_test
y_train=object.y_train
y_test=object.y_test



model = Sequential([
    Dense(units=1, activation='sigmoid', input_shape=(x_train.shape[1],)),
    Dense(units=1, activation='sigmoid')
])
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

history = model.fit(x_train, y_train, epochs=500, batch_size=32)

loss, accuracy = model.evaluate(x_test, y_test)
print(f'Accuracy: {accuracy}')


y_pred = model.predict(x_test)
y_pred_binary = (y_pred > 0.5).astype(int)

precision = precision_score(y_test, y_pred_binary)
recall = recall_score(y_test, y_pred_binary)
f1 = f1_score(y_test, y_pred_binary)
roc_auc = roc_auc_score(y_test, y_pred_binary)

print(f"Accuracy: {accuracy}")
print(f"precision: {precision}")

print(f"recall: {recall}")

print(f"f1: {f1}")
print(f"roc_auc: {roc_auc}")


conf_matrix = confusion_matrix(y_test, y_pred_binary)

plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', cbar=False)
plt.title('Confusion Matrix')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.show()
