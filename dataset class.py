import pandas as pd
import pyreadr

class DataSet:
    def __init__(self, path):
        self.filepath = path
        self.dataset = pd.DataFrame([])
        self.target_var = []
        self.covariates = []

    def __len__(self):
        return self.dataset.shape[0]

    def __getitem__(self, index):
        return self.dataset.iloc[index]

    def get_target(self):
        return self.dataset[self.target_var]

    def get_covariate(self):
        return self.dataset[self.covariates]

class ACICDataSet(DataSet):
    def __init__(self, path, target):
        super(ACICDataSet, self).__init__(path)
        dataset = pyreadr.read_r(self.filepath)
        self.dataset = dataset[list(dataset.keys())[0]]
        self.target_var = target
        self.covariates = list(self.dataset)
        for variables in self.target_var:
            self.covariates.remove(variables)

class MIMICDataSet(DataSet):
    def __init__(self, path, target):
        super(MIMICDataSet, self).__init__(path)
        self.dataset = pd.read_csv(self.filepath)
        self.target_var = target
        self.covariates = list(self.dataset)
        for variables in self.target_var:
            self.covariates.remove(variables)
