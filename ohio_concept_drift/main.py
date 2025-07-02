from ohio_concept_drift import resources
from ohio_concept_drift import geometry
from ohio_concept_drift import plotter
import pandas as pd
from ohio_concept_drift.warsaw_surveys import assign_district_and_vistula_bank


def run():
    ohio_dataset = resources.load_ohio_arff()
    ohio_dataset['ML_region'] = ohio_dataset['ML_region'].str.decode('utf-8')
    grouped_number_of_instances_by_region = ohio_dataset.groupby('ML_region').agg(number_of_instances=('ML_region', 'count'))

    grouped_drift_detection_by_region = resources.load_detected_drift().groupby('region').agg(total_drift_detection=('drift_type', 'count'))
    grouped_drift_detection_by_region['total_drift_detection'] = grouped_drift_detection_by_region['total_drift_detection'].astype('Int64')

    ohio_cities = geometry.ohio_cites_geopandas()

    ohio_results = pd.merge(ohio_cities, grouped_drift_detection_by_region, left_on='ML_region', right_on='region', how='left')
    ohio_results = pd.merge(ohio_results, grouped_number_of_instances_by_region, on='ML_region', how='left')

    ohio_results['total_drift_detection'] = ohio_results['total_drift_detection'].fillna(0)
    ohio_results['number_of_instances'] = ohio_results['number_of_instances'].fillna(0)
    ohio_results['drift_frequency_per_10k'] = 10000 * ohio_results['total_drift_detection'] / ohio_results['number_of_instances']

    plotter.plot_ohio_state(ohio_results, column_name='total_drift_detection', file_name='number_of_detection.pdf', vmax=10)
    plotter.plot_ohio_state(ohio_results, column_name='number_of_instances', file_name='number_of_instances.pdf', vmax=20000)
    plotter.plot_ohio_state(ohio_results, column_name='drift_frequency_per_10k', file_name='drift_frequency_per_10k.pdf', vmax=5)

    plotter.plot_ohio_state(ohio_results)


def district_and_vistula_bank():
    warsaw_surveys = assign_district_and_vistula_bank()
    warsaw_surveys.to_csv('resources/CITIZENS_W1_W2_5_1_1_fixed_merged(in)_with_vistula_district_and_bank.csv', encoding='UTF-8', sep=';', decimal='.',
                          index=False)
