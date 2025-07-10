from ohio_concept_drift import resources
import pandas as pd


def latex_ohio():
    ohio_arff = resources.load_ohio_arff()
    ohio_arff['ML_region'] = ohio_arff['ML_region'].str.decode('utf-8')
    ohio_arff['label'] = ohio_arff['label'].str.decode('utf-8')

    ohio_arff.loc[ohio_arff['label'] == '11.0', 'label'] = 'CAR'  # Auto/van/truck driver
    ohio_arff.loc[ohio_arff['label'] == '13.0', 'label'] = 'CAR'  # Carpool driver
    ohio_arff.loc[ohio_arff['label'] == '15.0', 'label'] = 'CAR'  # Vanpool driver
    ohio_arff.loc[ohio_arff['label'] == '17.0', 'label'] = 'PT'  # Bus (public transit)
    ohio_arff.loc[ohio_arff['label'] == '18.0', 'label'] = 'PT'  # School Bus
    ohio_arff.loc[ohio_arff['label'] == '19.0', 'label'] = 'PT'  # Taxi/paid limo
    ohio_arff.loc[ohio_arff['label'] == '20.0', 'label'] = 'WALK'  # Walk
    ohio_arff.loc[ohio_arff['label'] == '21.0', 'label'] = 'BIKE'  # Bicycle
    ohio_arff.loc[ohio_arff['label'] == '22.0', 'label'] = 'BIKE'  # Motorcycle, moped
    ohio_arff.loc[ohio_arff['label'] == '97.0', 'label'] = 'OTHER'  # Other (specify)
    ohio_arff.loc[ohio_arff['label'] == '99.0', 'label'] = 'OTHER'  # DK/RF

    grouped_by_region = ohio_arff.groupby('ML_region').agg(number_of_instances_in_region=('label', 'count')).reset_index()
    grouped_by_region_and_tmc = ohio_arff.groupby(['ML_region', 'label']).agg(number_of_instances=('label', 'count')).reset_index()
    pivoted = grouped_by_region_and_tmc.pivot(index='ML_region', columns='label', values='number_of_instances').reset_index()

    result = pd.merge(grouped_by_region, pivoted, on='ML_region', how='left')

    sum_row = result[['number_of_instances_in_region', 'BIKE', 'CAR', 'OTHER', 'PT', 'WALK']].sum()
    sum_row.name = 'Total'  # optional: name the row
    result = pd.concat([result, pd.DataFrame([sum_row])])

    result['car_ratio'] = 100 * result['CAR'] / result['number_of_instances_in_region']
    result['pt_ratio'] = 100 * result['PT'] / result['number_of_instances_in_region']
    result['walk_ratio'] = 100 * result['WALK'] / result['number_of_instances_in_region']
    result['bike_ratio'] = 100 * result['BIKE'] / result['number_of_instances_in_region']
    result['other_ratio'] = 100 * result['OTHER'] / result['number_of_instances_in_region']

    result = result[['ML_region', 'number_of_instances_in_region', 'CAR', 'car_ratio', 'PT', 'pt_ratio', 'WALK', 'walk_ratio', 'BIKE', 'bike_ratio', 'OTHER',
                     'other_ratio']]

    latex = result.to_latex(index=False, float_format="{:.2f}".format)
    print(latex)


def latex_warsaw():
    warsaw = resources.load_warsaw_surveys_with_district()
    clazz = 'label'
    warsaw.loc[warsaw[clazz] == 'CITY_BIKE', clazz] = 'BIKE'
    warsaw.loc[warsaw[clazz] == 'PRIVATE_BIKE', clazz] = 'BIKE'
    warsaw.loc[warsaw[clazz] == 'MIXED_BIKE_AND_OTHER', clazz] = 'BIKE'
    warsaw.loc[warsaw[clazz] == 'MIXED_CAR_AND_OTHER', clazz] = 'CAR'
    warsaw.loc[warsaw[clazz] == 'PUBLIC_TRANSPORT', clazz] = 'PT'
    warsaw.loc[warsaw[clazz] == 'WALKING_ONLY', clazz] = 'WALK'
    warsaw.loc[warsaw[clazz] == 'MULTIMODE', clazz] = 'OTHER'
    warsaw.loc[warsaw[clazz] == 'BIKE', clazz] = 'BIKE'
    warsaw.loc[warsaw[clazz] == 'PUBLIC_TRANSPORT', clazz] = 'PT'
    warsaw.loc[warsaw[clazz] == 'CAR', clazz] = 'CAR'
    warsaw.loc[warsaw[clazz] == 'OTHER', clazz] = 'OTHER'

    grouped_by_region = warsaw.groupby('vistula_bank').agg(number_of_instances_in_region=('travelAggregation', 'count')).reset_index()
    grouped_by_region_and_tmc = warsaw.groupby(['vistula_bank', 'travelAggregation']).agg(number_of_instances=('travelAggregation', 'count')).reset_index()
    pivoted = grouped_by_region_and_tmc.pivot(index='vistula_bank', columns='travelAggregation', values='number_of_instances').reset_index()

    result = pd.merge(grouped_by_region, pivoted, on='vistula_bank', how='left')

    sum_row = result[['number_of_instances_in_region', 'BIKE', 'CAR', 'OTHER', 'PT', 'WALK']].sum()
    sum_row.name = 'Total'  # optional: name the row
    result = pd.concat([result, pd.DataFrame([sum_row])])

    result['car_ratio'] = 100 * result['CAR'] / result['number_of_instances_in_region']
    result['pt_ratio'] = 100 * result['PT'] / result['number_of_instances_in_region']
    result['walk_ratio'] = 100 * result['WALK'] / result['number_of_instances_in_region']
    result['bike_ratio'] = 100 * result['BIKE'] / result['number_of_instances_in_region']
    result['other_ratio'] = 100 * result['OTHER'] / result['number_of_instances_in_region']

    result = result[['vistula_bank', 'number_of_instances_in_region', 'CAR', 'car_ratio', 'PT', 'pt_ratio', 'WALK', 'walk_ratio', 'BIKE', 'bike_ratio', 'OTHER',
                     'other_ratio']]

    latex = result.to_latex(index=False, float_format="{:.2f}".format)
    print(latex)
