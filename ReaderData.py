import  pandas as pd
from matplotlib import pyplot as plt
from sklearn.preprocessing import LabelEncoder
import seaborn as sns

# List of columns to plot


class ReaderData:
    def cap_outliers(dataset, col):
        q1 = dataset[col].quantile(0.25)
        q3 = dataset[col].quantile(0.75)
        iqr = q3 - q1
        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr
        dataset[col] = dataset[col].clip(lower=lower_bound, upper=upper_bound)
    def __init__(self):

        dataset = pd.read_csv("G:\\D\\MachineLearning\\smook\\cleaned_smoker_data2.csv")
        #dataset = pd.read_csv("G:\\D\\MachineLearning\\smook\\Data.csv")

        for col in dataset.columns:
            print (dataset[col].describe())
        #dataset['Smoker'] = dataset['Smoker'].map({'yes': 1, 'no': 0})
        #dataset['Gender'] = dataset['Gender'].map({'male': 1, 'female': 0})
        #dataset['Region'] = dataset['Region'].map({'north': 1, 'south': 0})

        dataset.hist(bins=30, figsize=(10, 10))
        plt.show()

       # duplicate_counts = dataset.duplicated(
        #    subset=['Age', 'Gender', 'BMI', 'Region', 'No. Childred', 'Insurance Charges', 'Smoker'])

        # Print the duplicate counts
        #print("Sum ",duplicate_counts.sum())
        #dataset.drop_duplicates().to_csv('dataset_after_cleaned.csv', index=False)
        #dataset['Age'] = dataset['Age'].round().astype(int)

        ReaderData.vislizeBokPlot(self , dataset)
       #ReaderData.cleanData(self ,dataset)
        self.dataset = dataset

    def vislizeBokPlot(self , dataset):
        columns = ['Age', 'BMI', 'No. Childred', 'Insurance Charges', 'Gender', 'Region']
        plt.figure(figsize=(10, 6))
        for i, column in enumerate(dataset.columns[:-1], 1):  # Exclude 'Diabetic' column for box plots
            plt.subplot(3, 3, i)
            sns.boxplot(y=dataset[column])
            plt.title(f'Box Plot of {column}')

        plt.tight_layout()
        plt.show()

    def cleanData(self, dataset):
        cols =['Insurance Charges' , 'BMI']
        for col in cols:
            ReaderData.cap_outliers(dataset ,col)
        dataset.to_csv('cleaned_smoker_data2.csv', index=False)



obj = ReaderData()
