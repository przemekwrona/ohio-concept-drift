from shapely import Point

from ohio_concept_drift.city.warsaw import Warsaw
from ohio_concept_drift import resources

import pandas as pd


def assign_district_and_vistula_bank():
    warsaw = Warsaw()
    warsaw_surveys = resources.load_warsaw_surveys()
    start_point = warsaw_surveys.apply(lambda row: Point(row['startingAddressLongitude_SURVEY'], row['startingAddressLatitude_SURVEY']), axis=1)
    warsaw_surveys[['district', 'vistula_bank']] = start_point.apply(warsaw.get_district).apply(pd.Series)
    return warsaw_surveys
