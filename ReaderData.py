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
        #dataset['Smoker'] = dataset['Smoker'].map({'yes': 1, 'no': 0})
        #dataset['Gender'] = dataset['Gender'].map({'male': 1, 'female': 0})
        #dataset['Region'] = dataset['Region'].map({'north': 1, 'south': 0})
        #dataset['Age'] = dataset['Age'].round().astype(int)

        #ReaderData.vislizeBokPlot(self , dataset)
        #ReaderData.cleanData(self ,dataset)
        self.dataset = dataset

    def vislizeBokPlot(self , data):
        columns = ['Age', 'BMI', 'No. Childred', 'Insurance Charges', 'Gender', 'Region']
        for col in columns:
            sns.boxplot(y=data[col])
            plt.title(f'Box Plot of {col}')
            plt.show()

    def cleanData(self, dataset):
        cols =['Insurance Charges' , 'BMI']
        for col in cols:
            ReaderData.cap_outliers(dataset ,col)
        dataset.to_csv('cleaned_smoker_data2.csv', index=False)



obj = ReaderData()
