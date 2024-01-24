import pandas as pd
from chefboost import Chefboost as chef
from sklearn.model_selection import train_test_split

dataset = pd.read_csv("G:\\D\\MachineLearning\\smook\\dataset_after_cleaned.csv")
dataset['Smoker'] = dataset['Smoker'].map({1: 'yes', 0: 'no'})
dataset['Gender'] = dataset['Gender'].map({1: 'male', 0: 'female'})
dataset['Region'] = dataset['Region'].map({1: 'north', 0: 'south'})
train_data, test_data = train_test_split(dataset, test_size=0.2, random_state=0)
print (pd.DataFrame(test_data).head())
config = {'algorithm': 'C4.5'}


model = chef.fit(train_data, config = config, target_label = 'Smoker' , num_cores=1)

test_data_for_prediction = test_data.drop(columns=['Smoker'])

predictions = []

for i in range(test_data_for_prediction.shape[0]):
    row_df = test_data_for_prediction.iloc[i]

    single_row_prediction = chef.predict(model, row_df)

    predictions.append(single_row_prediction[0])

test_data['Predictions'] = predictions

print(test_data.head())

