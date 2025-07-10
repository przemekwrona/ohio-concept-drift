from ohio_concept_drift.warsaw_surveys import assign_district_and_vistula_bank
import csv2arff
import argparse


def arff_warsaw_surveys():
    warsaw_surveys = assign_district_and_vistula_bank()

    # Get columns starting with
    surveys = warsaw_surveys[
        [col for col in warsaw_surveys.columns if col.endswith(('_SURVEY', '_TRANSIT', '_WALK', '_CAR')) and not col.endswith('_LOW_TRANSIT')]]
    surveys['district'] = warsaw_surveys['district'].copy()
    surveys['vistula_bank'] = warsaw_surveys['vistula_bank'].copy()
    surveys['label'] = warsaw_surveys['travelAggregation'].copy()

    # Aggregate label classes
    surveys.loc[surveys['label'] == 'PRIVATE_BIKE', 'label'] = 'BIKE'
    surveys.loc[surveys['label'] == 'CITY_BIKE', 'label'] = 'BIKE'
    surveys.loc[surveys['label'] == 'MIXED_BIKE_AND_OTHER', 'label'] = 'BIKE'
    surveys.loc[surveys['label'] == 'MIXED_CAR_AND_OTHER', 'label'] = 'CAR'
    surveys.loc[surveys['label'] == 'MULTIMODE', 'label'] = 'OTHER'

    # Drop columns
    surveys = surveys.drop(columns=[
        "id_SURVEY",
        "startingTime_SURVEY",
        "endingTime_SURVEY",
        "FirstStopName_TRANSIT",
        "lineNumber_SURVEY",
        "describedDay_SURVEY",

        "PlanType_WALK",
        "PlanType_TRANSIT",
        "PlanType_CAR",

        "cnPath_WALK",
        "cnPath_CAR",
        "cnPath_TRANSIT",
        "cnTransportModes_WALK",
        "cnTransportModes_CAR",
        "cnTransportModes_TRANSIT",

        "homeAddressGeocoding_SURVEY",
        "startingAddressGeocoding_SURVEY",
        "loca11ationGeocoding_SURVEY"
    ], axis='columns')

    csv_file_name = 'CITIZENS_W1_W2_5_1_1_fixed_merged(in)_with_vistula_district_and_bank'
    surveys.to_csv(f"resources/{csv_file_name}.csv", encoding='UTF-8', sep=';', decimal='.', index=False)

    args = argparse.Namespace(
        input=f"resources/{csv_file_name}.csv",
        output=f"resources/{csv_file_name}.arff",
        name="warsaw_surveys",
        delimiter=';'
    )

    csv2arff.Csv2Arff(args)
