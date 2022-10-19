import pandas as pd
import random as rd
import numpy as np

class Dataset:
    def __init__(self, filename):
        self.filename = filename
        self.df = None

    def load(self):
        # file = open(self.filename)
        self.df = pd.read_csv(self.filename)

    def get_random_row(self):
        np_array = self.df.to_numpy();
        rand_row = rd.randint(0, len(np_array[0]))
        return np_array[rand_row]

