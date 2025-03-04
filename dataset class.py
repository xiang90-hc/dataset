import pandas as pd

class DataSet:
    def __init__(self, path):
        self.filepath = path
        self.dataset = pd.read_csv(self.filepath)

    def __len__(self):
        return self.dataset.shape[0]

    def __getitem__(self, index):
        return self.dataset.iloc[index]


class CovDataSet(DataSet):
    def __init__(self, path, target):
        super(CovDataSet, self).__init__(path)
        self.target_var = target

    def get_target(self):
        return self.dataset[self.target_var]

    def get_covariate(self):
        index = list(self.dataset)
        target_index = []
        for variables in self.target_var:
            index.remove(variables)

        return self.dataset[index]
