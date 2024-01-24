import pandas as pd
from chefboost import Chefboost as chef
from sklearn.model_selection import train_test_split

dataset = pd.read_csv("/content/sample_data/dataset_after_cleaned.csv")
dataset['Smoker'] = dataset['Smoker'].map({1: 'yes', 0: 'no'})
dataset['Gender'] = dataset['Gender'].map({1: 'male', 0: 'female'})
dataset['Region'] = dataset['Region'].map({1: 'north', 0: 'south'})
train_data, test_data = train_test_split(dataset, test_size=0.2, random_state=0)
print (pd.DataFrame(test_data).head())
config = {'algorithm': 'C4.5'}


model = chef.fit(train_data, config = config, target_label = 'Smoker')

test_data_for_prediction = test_data.drop(columns=['Smoker'])

predictions = []

for i in range(test_data_for_prediction.shape[0]):
    row_df = test_data_for_prediction.iloc[i]

    single_row_prediction = chef.predict(model, row_df)

    predictions.append(single_row_prediction)

test_data['Predictions'] = predictions

print(test_data.head())

from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import seaborn as sns
import matplotlib.pyplot as plt
cm = confusion_matrix(test_data['Smoker'], test_data['Predictions'])
sns.heatmap(cm, annot=True, fmt='g', cmap='Blues', cbar=False)
plt.title('Confusion Matrix')
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.show()




label_mapping = {'yes': 1, 'no': 0}
test_data['Smoker'] = test_data['Smoker'].map(label_mapping)
test_data['Predictions'] = test_data['Predictions'].map(label_mapping)


accuracy = accuracy_score(test_data['Smoker'], test_data['Predictions'])
precision = precision_score(test_data['Smoker'], test_data['Predictions'], average='weighted')
recall = recall_score(test_data['Smoker'], test_data['Predictions'], average='weighted')
f1 = f1_score(test_data['Smoker'], test_data['Predictions'], average='weighted')

roc_auc = roc_auc_score(test_data['Smoker'], test_data['Predictions'])

print("Confusion Matrix:")
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1 Score:", f1)
print("ROC AUC Score:", roc_auc)