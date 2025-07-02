from ohio_concept_drift import resources
from ohio_concept_drift import geometry
from ohio_concept_drift import plotter
import pandas as pd


def ohio_data_frame():
    ohio_dataset = resources.load_ohio_arff()
    ohio_dataset['ML_region'] = ohio_dataset['ML_region'].str.decode('utf-8')
    grouped_number_of_instances_by_region = ohio_dataset.groupby('ML_region').agg(number_of_instances=('ML_region', 'count'))

    ohio_detected_drift = resources.load_detected_drift()
    grouped_drift_detection_by_region = ohio_detected_drift.groupby('region').agg(total_drift_detection=('drift_type', 'count'),
                                                                                  first_occurrence_index=('instance_index', 'min'),
                                                                                  last_occurrence_index=('instance_index', 'max'))
    grouped_drift_detection_by_region['total_drift_detection'] = grouped_drift_detection_by_region['total_drift_detection'].astype('Int64')
    grouped_drift_detection_by_region['first_occurrence_index'] = grouped_drift_detection_by_region['first_occurrence_index'].astype('Int64')
    grouped_drift_detection_by_region['last_occurrence_index'] = grouped_drift_detection_by_region['last_occurrence_index'].astype('Int64')

    ohio_cities = geometry.ohio_cites_geopandas()

    ohio_results = pd.merge(ohio_cities, grouped_drift_detection_by_region, left_on='ML_region', right_on='region', how='left')
    ohio_results = pd.merge(ohio_results, grouped_number_of_instances_by_region, on='ML_region', how='left')

    ohio_results['total_drift_detection'] = ohio_results['total_drift_detection'].fillna(0)
    ohio_results['number_of_instances'] = ohio_results['number_of_instances'].fillna(0)
    ohio_results['drift_frequency_per_10k'] = 10000 * ohio_results['total_drift_detection'] / ohio_results['number_of_instances']
    ohio_results['first_occurrence_ratio'] = 100 * ohio_results['first_occurrence_index'] / ohio_results['number_of_instances']
    ohio_results['last_occurrence_ratio'] = 100 * ohio_results['last_occurrence_index'] / ohio_results['number_of_instances']

    return ohio_results


def plot_ohio():
    ohio_results = ohio_data_frame()

    plotter.plot_ohio_state(ohio_results, column_name='total_drift_detection', file_name='number_of_detection.pdf', vmax=10)
    plotter.plot_ohio_state(ohio_results, column_name='number_of_instances', file_name='number_of_instances.pdf', vmax=20000)
    plotter.plot_ohio_state(ohio_results, column_name='drift_frequency_per_10k', file_name='drift_frequency_per_10k.pdf', vmax=5)
    plotter.plot_ohio_state(ohio_results, column_name='first_occurrence_index', file_name='first_occurrence_ratio.pdf')
    plotter.plot_ohio_state(ohio_results, column_name='last_occurrence_index', file_name='last_occurrence_ratio.pdf')
