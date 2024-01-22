import  pandas as pd

class ReaderData:
    def __init__(self):
        dataset = pd.read_csv("G:\\D\\MachineLearning\\smook\\Data.csv")


        self.dataset = dataset


obj = ReaderData()