import pandas as pd
from scipy.io import arff

OHIO_PATH = 'resources/AllOhioDataSorted_2.arff'
DRIFT_PATH = 'resources/drift_log.csv'


def load_ohio_arff():
    # Load the .arff file
    data, meta = arff.loadarff(OHIO_PATH)

    # Convert to Pandas DataFrame
    df = pd.DataFrame(data)

    # If any columns are byte strings, decode them (optional)
    # for col in df.select_dtypes([object]):
    #     df[col] = df[col].str.decode('utf-8')

    return df


def load_detected_drift():
    df = pd.read_csv(DRIFT_PATH)

    return df


def load_warsaw_surveys():
    return pd.read_csv('resources/CITIZENS_W1_W2_5_1_1_fixed_merged(in).csv', encoding='ISO-8859-1', sep=';', decimal='.')
