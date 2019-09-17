# File for predicting data using the trained model
# from the previous step
import os
import pandas as pd

from sklearn.externals import joblib

FILE = os.getenv('CSV_FILE')
COLUMNS = os.getenv('COLUMNS').split(';')
MODEL = os.getenv('MODEL')
OUT_PATH = os.getenv('OUT_PATH')


def main():
    if not COLUMNS:
        data = pd.read_csv(FILE)
    else:
        data = pd.read_csv(FILE, usecols=COLUMNS)

    km = joblib.load(MODEL)
    y_means = km.fit_predict(data)

    data['Prediction'] = y_means.tolist()
    data.to_csv(OUT_PATH)
