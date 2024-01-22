import  pandas as pd
import matplotlib.pyplot as plt
import scipy
import seaborn as sns
from sklearn.compose import ColumnTransformer

from sklearn.model_selection import train_test_split

from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from ReaderData import ReaderData


class Main:
        def __init__(self):
            data = ReaderData().dataset
            smoker_dist = data['Smoker'].value_counts()
            data['Smoker']=data['Smoker'].map({'yes':1 ,'no' :0})

            smoker_dist.plot(kind='bar')
            plt.title('Distribution of Smoker Class')
            plt.xlabel('Smoker')
            plt.ylabel('Frequency')
            plt.show()

            # desnity of ages

            plt.figure(figsize=(10 ,6))
            data['Age'].plot(kind='density')
            plt.title('Density of Age')
            plt.xlabel('Ages')
            plt.ylabel('Density')
            plt.show()


            plt.figure(figsize=(10,6))
            data['BMI'].plot(kind='density')
            plt.title('Density of BMI')
            plt.xlabel('BMI')
            plt.ylabel('Density')
            plt.show()


            x = data[['Age' , 'Insurance Charges']]
            y = data['Smoker']


            plt.figure(figsize=(12, 8))
            sns.scatterplot(data=data, x='Age', y='Insurance Charges', hue='Smoker')
            plt.title('Scatter Plot of Age vs. BMI, Colored by Region')
            plt.xlabel('Age')
            plt.ylabel('Insurance Charges')
            plt.show()

            Gender = pd.get_dummies(data.Gender)
            Region = pd.get_dummies(data.Region)
            data = pd.concat([data, Gender, Region], axis='columns')
            data = data.drop(['Gender', 'Region'], axis='columns')

            print(data.head())



           # cat_colmn  = ['Gender','Region']
            #column_transformer = ColumnTransformer([('one_hot_encoder' , OneHotEncoder() , cat_colmn)] , remainder='passthrough')
            #x_transformed = column_transformer.fit_transform(x)

            #print("data after transformed : " , pd.DataFrame(x_transformed).head())

            correlation_matrix = data.corr()
            print("correlation matrix:\n", correlation_matrix)
            sns.heatmap(correlation_matrix, annot=True, linewidths=.5, cmap='coolwarm')
            plt.title('Correlation Heatmap')
            plt.show()

            scaler = MinMaxScaler()


            print("x shape : " , x.shape)
            print("y shape : " , y.shape)

            X_transformed = scaler.fit_transform(x)

            X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.20, random_state=0)


            self.x_train = X_train
            self.x_test = X_test
            self.y_train = y_train
            self.y_test = y_test






object = Main()