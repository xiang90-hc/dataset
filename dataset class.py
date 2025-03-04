import pandas as pd

class DataSet:
    def __init__(self, path):
        self.filepath = path

    def __len__(self):
        dataset = pd.read_csv(self.filepath)
        return dataset.shape[0]

    def __getitem__(self, index):
        dataset = pd.read_csv(self.filepath)
        return dataset.iloc[index]
