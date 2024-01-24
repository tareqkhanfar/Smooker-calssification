import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    "Model": ["KNN (k=3)", "KNN (k=5)", "KNN (k=7)", "Naive Bayes", "Decision Tree", "ANN"],
    "TN": [389, 381, 381, 367, 378, 359],
    "FP": [19, 27, 27, 41, 30, 49],
    "FN": [29, 25, 25, 67, 34, 25],
    "TP": [156, 160, 160, 118, 151, 160],
    "Accuracy": [92, 91, 91, 82, 89.2, 87.3],
    "Precision": [89.6, 86, 85, 74, 89.1, 76.1],
    "Recall": [84, 86, 86, 64, 89.2, 86.4],
    "F1 Score": [87, 86, 86, 69, 89.1, 81.1],
    "ROC": [95, 96, 96.6, 92, 87, 87.1]
}


df = pd.DataFrame(data)
df.plot (x='Model' , y=['Accuracy' , 'Precision' , "Recall", "F1 Score" , "ROC"], kind='bar')
plt.show()


df.plot (x='Model' , y=["TN", "FP", "FN", "TP"], kind='bar')
plt.show()

