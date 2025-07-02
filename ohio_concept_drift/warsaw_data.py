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

    grouped_by_district = warsaw_surveys.groupby('district').agg(number_of_instances_in_district=('id_SURVEY', 'count'))
    grouped_by_vistula_bank = warsaw_surveys.groupby('vistula_bank').agg(number_of_instances_in_vistula_bank=('id_SURVEY', 'count'))

    warsaw_detected_drift = resources.load_warsaw_detected_drift()
    grouped_detected_drift_by_vistula_bank = warsaw_detected_drift.groupby('region').agg(number_of_drift_detection=('instance_index', 'count'))

    warsaw_district_results = pd.merge(warsaw_districts, grouped_by_district, left_on='district', right_on='district', how='left')

    warsaw_vistula_bank_results = pd.merge(warsaw_districts, grouped_by_vistula_bank, left_on='ML_region', right_on='vistula_bank', how='left')
    warsaw_vistula_bank_results = pd.merge(warsaw_vistula_bank_results, grouped_detected_drift_by_vistula_bank, left_on='ML_region', right_on='region', how='left')

    warsaw_vistula_bank_results['drift_frequency_per_10k'] = 10000 * warsaw_vistula_bank_results['number_of_drift_detection'] / warsaw_vistula_bank_results['number_of_instances_in_vistula_bank']

    plotter.plot_warsaw(warsaw_district_results, column_name='number_of_instances_in_district', file_name='warsaw/number_of_instances_in_district.pdf', vmax=1000)
    plotter.plot_warsaw(warsaw_vistula_bank_results, column_name='number_of_instances_in_vistula_bank', file_name='warsaw/number_of_instances_in_vistula_bank.pdf', vmax=20000)
    plotter.plot_warsaw(warsaw_vistula_bank_results, column_name='number_of_drift_detection', file_name='warsaw/number_of_drift_detection_in_vistula_bank.pdf', vmax=20)
    plotter.plot_warsaw(warsaw_vistula_bank_results, column_name='drift_frequency_per_10k', file_name='warsaw/drift_frequency_per_10k.pdf', vmax=100)
