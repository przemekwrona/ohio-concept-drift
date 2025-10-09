import pandas as pd
from scipy.io import arff

OHIO_PATH = 'resources/AllOhioDataSorted_2.arff'

USA_PATH = 'resources/NHTSDataSorted.arff'

WARSAW_DRIFT_PATH = 'resources/warsaw_drift_log.csv'


def load_ohio_arff():
    data, meta = arff.loadarff(OHIO_PATH)
    return pd.DataFrame(data)


def load_usa_arff():
    data, meta = arff.loadarff(USA_PATH)
    return pd.DataFrame(data)


def load_detected_drift(drift_path):
    return pd.read_csv(drift_path)


def load_ohio_detected_drift(drift_results_directory):
    return load_detected_drift(f"{drift_results_directory}/drift_log.csv")


def load_warsaw_detected_drift():
    return pd.read_csv(WARSAW_DRIFT_PATH)


def load_warsaw_surveys():
    return pd.read_csv('resources/CITIZENS_W1_W2_5_1_1_fixed_merged(in).csv', encoding='ISO-8859-1', sep=';', decimal='.')


def load_warsaw_surveys_with_district():
    return pd.read_csv('resources/CITIZENS_W1_W2_5_1_1_fixed_merged(in)_with_vistula_district_and_bank.csv', encoding='UTF-8', sep=';', decimal='.')
