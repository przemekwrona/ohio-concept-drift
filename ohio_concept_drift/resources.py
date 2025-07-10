import pandas as pd
from scipy.io import arff

OHIO_PATH = 'resources/AllOhioDataSorted_2.arff'
OHIO_DRIFT_PATH = 'resources/drift_log.csv'
WARSAW_DRIFT_PATH = 'resources/warsaw_drift_log.csv'


def load_ohio_arff():
    data, meta = arff.loadarff(OHIO_PATH)
    return pd.DataFrame(data)


def load_ohio_detected_drift(drift_results_directory):
    return pd.read_csv(f"{drift_results_directory}/drift_log.csv")


def load_warsaw_detected_drift():
    return pd.read_csv(WARSAW_DRIFT_PATH)


def load_warsaw_surveys():
    return pd.read_csv('resources/CITIZENS_W1_W2_5_1_1_fixed_merged(in).csv', encoding='ISO-8859-1', sep=';', decimal='.')


def load_warsaw_surveyss():
    return pd.read_csv('resources/CITIZENS_W1_W2_5_1_1_fixed_merged(in)_with_vistula_district_and_bank.csv', encoding='UTF-8', sep=';', decimal='.')
