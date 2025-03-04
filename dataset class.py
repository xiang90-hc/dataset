import pandas as pd

class DataSet:
    def __init__(self, path, target):
        self.filepath = path
        self.dataset = pd.read_csv(self.filepath)
        self.target_var = target
        self.covariates = list(self.dataset)
        for variables in self.target_var:
            self.covariates.remove(variables)

    def __len__(self):
        return self.dataset.shape[0]

    def __getitem__(self, index):
        return self.dataset.iloc[index]

    def get_target(self):
        return self.dataset[self.target_var]

    def get_covariate(self):
        return self.dataset[self.covariates]

    def get_covariate(self):
        index = list(self.dataset)
        for variables in self.target_var:
            index.remove(variables)

        return self.dataset[index]

