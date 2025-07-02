from ohio_concept_drift import resources
from ohio_concept_drift import geometry
from ohio_concept_drift import plotter
import pandas as pd
from ohio_concept_drift.city.warsaw import Warsaw


def warsaw_data_frame():
    warsaw = Warsaw()
    warsaw_districts = geometry.warsaw_districts_geopandas()
    warsaw_districts = warsaw_districts[warsaw_districts['name'] != 'Warszawa']
    warsaw_districts['district'] = warsaw_districts['name'].str.upper()
    warsaw_districts['ML_region'] = warsaw_districts['district'].apply(warsaw.map_district_to_vistula_bank)

    return warsaw_districts


def plot_warsaw():
    warsaw_districts = warsaw_data_frame()

    warsaw_surveys = resources.load_warsaw_surveyss()

    grouped_by_district = warsaw_surveys.groupby('district').agg(number_of_instances=('id_SURVEY', 'count'))
    grouped_by_vistula_bank = warsaw_surveys.groupby('vistula_bank').agg(number_of_instances=('id_SURVEY', 'count'))

    warsaw_district_results = pd.merge(warsaw_districts, grouped_by_district, left_on='district', right_on='district', how='left')
    warsaw_vistula_bank_results = pd.merge(warsaw_districts, grouped_by_vistula_bank, left_on='ML_region', right_on='vistula_bank', how='left')

    plotter.plot_warsaw(warsaw_district_results, column_name='number_of_instances', file_name='number_of_instances_in_district.pdf', vmax=1000)
    plotter.plot_warsaw(warsaw_vistula_bank_results, column_name='number_of_instances', file_name='number_of_instances_in_vistula_bank.pdf', vmax=20000)
