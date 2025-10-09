from ohio_concept_drift import resources
from ohio_concept_drift import geometry
from ohio_concept_drift import plotter
import pandas as pd
import os
import numpy as np


def load_drift_results(arff_dataset, detected_drift, regions):
    arff_dataset['ML_region'] = arff_dataset['ML_region'].str.decode('utf-8')
    grouped_number_of_instances_by_region = arff_dataset.groupby('ML_region').agg(number_of_instances=('ML_region', 'count'))

    grouped_drift_detection_by_region = detected_drift.groupby('region').agg(total_drift_detection=('drift_type', 'count'),
                                                                             first_occurrence_index=('instance_index', 'min'),
                                                                             last_occurrence_index=('instance_index', 'max'))
    grouped_drift_detection_by_region['total_drift_detection'] = grouped_drift_detection_by_region['total_drift_detection'].astype('Int64')
    grouped_drift_detection_by_region['first_occurrence_index'] = grouped_drift_detection_by_region['first_occurrence_index'].astype('Int64')
    grouped_drift_detection_by_region['last_occurrence_index'] = grouped_drift_detection_by_region['last_occurrence_index'].astype('Int64')

    ohio_results = pd.merge(regions, grouped_drift_detection_by_region, left_on='ML_region', right_on='region', how='left')
    ohio_results = pd.merge(ohio_results, grouped_number_of_instances_by_region, on='ML_region', how='left')

    ohio_results['total_drift_detection'] = ohio_results['total_drift_detection'].fillna(0)
    ohio_results['number_of_instances'] = ohio_results['number_of_instances'].fillna(0)
    ohio_results['first_occurrence_index'] = ohio_results['first_occurrence_index'].fillna(0)
    ohio_results['last_occurrence_index'] = ohio_results['last_occurrence_index'].fillna(0)
    np.where(ohio_results['number_of_instances'] > 0, 10000 * ohio_results['total_drift_detection'] / ohio_results['number_of_instances'], 0)

    ohio_results['drift_frequency_per_10k'] = np.where(ohio_results['number_of_instances'] > 0, 10000 * ohio_results['total_drift_detection'] / ohio_results['number_of_instances'], 0)
    ohio_results['first_occurrence_ratio'] = np.where(ohio_results['number_of_instances'] > 0, 10000 * ohio_results['first_occurrence_index'] / ohio_results['number_of_instances'], 0)
    ohio_results['last_occurrence_ratio'] = np.where(ohio_results['number_of_instances'] > 0, 10000 * ohio_results['last_occurrence_index'] / ohio_results['number_of_instances'], 0)

    return ohio_results


def ohio_data_frame(drift_results_directory):
    ohio_dataset = resources.load_ohio_arff()
    detected_drift = resources.load_ohio_detected_drift(drift_results_directory)
    ohio_cities = geometry.ohio_cites_geopandas()
    return load_drift_results(arff_dataset=ohio_dataset, detected_drift=detected_drift, regions=ohio_cities)


def usa_data_frame(drift_results_path):
    usa_dataset = resources.load_usa_arff()
    detected_drift = resources.load_detected_drift(drift_results_path)
    usa_states = geometry.usa_states_geopandas()

    return load_drift_results(arff_dataset=usa_dataset, detected_drift=detected_drift, regions=usa_states)


def load_ohio_data_per_experiment(experiment_name, drift_results_directory, column_name):
    ohio_results = ohio_data_frame(drift_results_directory)

    ohio_data = (ohio_results[['ML_region', column_name, 'number_of_instances']]
                 .groupby('ML_region').first().reset_index())
    ohio_data['10k'] = 10_000 * ohio_data[column_name] / ohio_data['number_of_instances']
    ohio_data_rename = ohio_data.rename(
        columns={column_name: experiment_name, '10k': f'{experiment_name}_10k', 'number_of_instances': f'{experiment_name}_total'})

    return ohio_data_rename[['ML_region', experiment_name, f'{experiment_name}_total', f'{experiment_name}_10k']]


def load_usa_data_per_experiment(experiment_name, drift_results_file, column_name):
    usa_results = usa_data_frame(drift_results_file)

    usa_data = (usa_results[['ML_region', column_name, 'number_of_instances']]
                 .groupby('ML_region').first().reset_index())
    usa_data['10k'] = np.where(usa_data['number_of_instances'] > 0, 10_000 * usa_data[column_name] / usa_data['number_of_instances'], 0)
    ohio_data_rename = usa_data.rename(
        columns={column_name: experiment_name, '10k': f'{experiment_name}_10k', 'number_of_instances': f'{experiment_name}_total'})

    return ohio_data_rename[['ML_region', experiment_name, f'{experiment_name}_total', f'{experiment_name}_10k']]


def plot_ohio(experiment_name, drift_results_directory):
    if not os.path.exists(f"ohio/{experiment_name}/"):
        os.makedirs(f"ohio/{experiment_name}/")

    ohio_results = ohio_data_frame(drift_results_directory)

    plotter.plot_ohio_state(ohio_results, column_name='total_drift_detection', file_name=f"ohio/{experiment_name}/number_of_detection.pdf", vmax=12, step=3,
                            is_gt_showed=True, label='Number of Drift Detection')
    plotter.plot_ohio_state(ohio_results, column_name='number_of_instances', file_name=f"ohio/{experiment_name}/number_of_instances.pdf", vmax=20000, step=5000,
                            label='Number of instances')
    plotter.plot_ohio_state(ohio_results, column_name='drift_frequency_per_10k', file_name=f"ohio/{experiment_name}/drift_frequency_per_10k.pdf", vmax=12,
                            step=3, is_gt_showed=True, label='Number of Detection per 10k instances')
    plotter.plot_ohio_state(ohio_results, column_name='first_occurrence_index', file_name=f"ohio/{experiment_name}/first_occurrence_ratio.pdf", vmax=140000,
                            step=20000, label='First drift detection')
    plotter.plot_ohio_state(ohio_results, column_name='last_occurrence_index', file_name=f"ohio/{experiment_name}/last_occurrence_ratio.pdf", vmax=140000,
                            step=20000, label='Last drift detection')


def plot_usa(experiment_name, drift_results_directory):
    # if not os.path.exists(f"usa/{experiment_name}/"):
    #     os.makedirs(f"ohio/{experiment_name}/")

    usa_results = usa_data_frame(drift_results_directory)

    # plotter.plot_ohio_state(ohio_results, column_name='total_drift_detection', file_name=f"ohio/{experiment_name}/number_of_detection.pdf", vmax=12, step=3,
    #                         is_gt_showed=True, label='Number of Drift Detection')
    plotter.plot_usa_states(usa_results, column_name='number_of_instances', file_name=f"usa/number_of_instances.pdf", vmax=200_000, step=25_000,
                            label='Number of instances')
    # plotter.plot_ohio_state(ohio_results, column_name='drift_frequency_per_10k', file_name=f"ohio/{experiment_name}/drift_frequency_per_10k.pdf", vmax=12,
    #                         step=3, is_gt_showed=True, label='Number of Detection per 10k instances')
    # plotter.plot_ohio_state(ohio_results, column_name='first_occurrence_index', file_name=f"ohio/{experiment_name}/first_occurrence_ratio.pdf", vmax=140000,
    #                         step=20000, label='First drift detection')
    # plotter.plot_ohio_state(ohio_results, column_name='last_occurrence_index', file_name=f"ohio/{experiment_name}/last_occurrence_ratio.pdf", vmax=140000,
    #                         step=20000, label='Last drift detection')
