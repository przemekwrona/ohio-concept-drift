from ohio_concept_drift import resources
from ohio_concept_drift import geometry
from ohio_concept_drift import plotter
import pandas as pd


def run():
    ohio_dataset = resources.load_ohio_arff()
    ohio_dataset['ML_region'] = ohio_dataset['ML_region'].str.decode('utf-8')
    grouped_sum = ohio_dataset.groupby('ML_region')['age'].mean()

    ohio_cities = geometry.ohio_cites_geopandas()

    ohio_results = pd.merge(ohio_cities, grouped_sum, on='ML_region', how='left')

    plotter.plot_ohio_state(ohio_results)
