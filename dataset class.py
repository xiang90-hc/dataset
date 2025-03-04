import csv

class DataSet:
    def __init__(self, path):
        self.filepath = path

    def __len__(self):
        length = 0
        with open(self.filepath, 'r') as dataset:
            csv_reader = csv.reader(dataset)
            for row in csv_reader:
                length += 1
        return length - 1

    def __getitem__(self, index):
        i = 0
        with open(self.filepath, 'r') as dataset:
            csv_reader = csv.reader(dataset)
            for row in csv_reader:
                if i == index + 1:
                    return row
                i += 1



