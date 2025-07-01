from ohio_concept_drift import resources
from ohio_concept_drift import geometry
from ohio_concept_drift import plotter
import pandas as pd


def run():
    ohio_dataset = resources.load_ohio_arff()
    ohio_dataset['ML_region'] = ohio_dataset['ML_region'].str.decode('utf-8')
    grouped_drift_detection_by_region = resources.load_detected_drift().groupby('region').agg(total_drift_detection=('drift_type', 'count'))
    grouped_drift_detection_by_region['total_drift_detection'] = grouped_drift_detection_by_region['total_drift_detection'].astype('Int64')

    ohio_cities = geometry.ohio_cites_geopandas()

    ohio_results = pd.merge(ohio_cities, grouped_drift_detection_by_region, left_on='ML_region', right_on='region', how='left')
    ohio_results['total_drift_detection'] = ohio_results['total_drift_detection'].fillna(0)

    plotter.plot_ohio_state(ohio_results, 'number_of_detection.pdf')

    plotter.plot_ohio_state(ohio_results)
