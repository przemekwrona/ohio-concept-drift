from ohio_concept_drift.warsaw_surveys import assign_district_and_vistula_bank


def arff_warsaw_surveys():
    warsaw_surveys = assign_district_and_vistula_bank()

    # Get columns starting with
    surveys = warsaw_surveys[
        [col for col in warsaw_surveys.columns if col.endswith(('_SURVEY', '_TRANSIT', '_WALK', '_CAR')) and not col.endswith('_LOW_TRANSIT')]]
    surveys['district'] = warsaw_surveys['district']
    surveys['vistula_bank'] = warsaw_surveys['vistula_bank']
    surveys['label'] = warsaw_surveys['travelAggregation']

    # Aggregate label classes
    surveys.loc[surveys['label'] == 'PRIVATE_BIKE', 'label'] = 'BIKE'
    surveys.loc[surveys['label'] == 'CITY_BIKE', 'label'] = 'BIKE'
    surveys.loc[surveys['label'] == 'MIXED_BIKE_AND_OTHER', 'label'] = 'BIKE'
    surveys.loc[surveys['label'] == 'MIXED_CAR_AND_OTHER', 'label'] = 'CAR'
    surveys.loc[surveys['label'] == 'MULTIMODE', 'label'] = 'OTHER'

    # Drop columns
    surveys = surveys.drop(columns=[
        "id_SURVEY",
        "PlanType_CAR",
        "loca11ationGeocoding_SURVEY",
        "startingTime_SURVEY",
        "describedDay_SURVEY",

        "homeAddressGeocoding_SURVEY",
        "startingAddressGeocoding_SURVEY",
        # "localisationGeocoding_SURVEY",
        "cnPath_WALK",
        "cnPath_CAR",
        "cnPath_TRANSIT",
        "cnTransportModes_WALK",
        "cnTransportModes_CAR",
        "PlanType_TRANSIT",
        "PlanType_WALK",
        "PlanType_WALK",
        "cnTransportModes_TRANSIT",
        "FirstStopName_TRANSIT",
        "FirstStopGeocoding_TRANSIT",

        "ParkingCost_CAR",
        "minCost_TRANSIT",
        "avgCost_TRANSIT",
        "maxCost_TRANSIT",

        "endingTime_SURVEY",
        "lineNumber_SURVEY"
    ], axis='columns')

    csv_file_name = 'CITIZENS_W1_W2_5_1_1_fixed_merged(in)_with_vistula_district_and_bank.csv'
    surveys.to_csv(f"resources/{csv_file_name}", encoding='UTF-8', sep=';', decimal='.', index=False)

    # surveys['district'] = surveys['district'].astype(str)
    # surveys['vistula_bank'] = surveys['vistula_bank'].astype(str)
    # surveys['usingCar_SURVEY'] = surveys['usingCar_SURVEY'].astype(bool)
    # surveys['parking_SURVEY'] = surveys['parking_SURVEY'].astype(bool)
    # surveys['journeyReasonsWarsawI16_SURVEY'] = surveys['journeyReasonsWarsawI16_SURVEY'].astype(bool)
    # surveys['factorsPublicTransportWarsawI1_SURVEY'] = surveys['factorsPublicTransportWarsawI1_SURVEY'].astype(bool)
    # surveys['factorsPublicTransportWarsawI2_SURVEY'] = surveys['factorsPublicTransportWarsawI2_SURVEY'].astype(bool)
    # surveys['factorsPublicTransportWarsawI3_SURVEY'] = surveys['factorsPublicTransportWarsawI3_SURVEY'].astype(bool)
    # surveys['factorsPublicTransportWarsawI4_SURVEY'] = surveys['factorsPublicTransportWarsawI4_SURVEY'].astype(bool)
    # surveys['factorsPublicTransportWarsawI5_SURVEY'] = surveys['factorsPublicTransportWarsawI5_SURVEY'].astype(bool)
    # surveys['factorsPublicTransportWarsawI6_SURVEY'] = surveys['factorsPublicTransportWarsawI6_SURVEY'].astype(bool)
    # surveys['factorsPublicTransportWarsawI7_SURVEY'] = surveys['factorsPublicTransportWarsawI7_SURVEY'].astype(bool)
    # surveys['factorsPublicTransportWarsawI9_SURVEY'] = surveys['factorsPublicTransportWarsawI9_SURVEY'].astype(bool)
    # surveys['factorsPublicTransportWarsawI10_SURVEY'] = surveys['factorsPublicTransportWarsawI10_SURVEY'].astype(bool)
    # surveys['factorsPublicTransportWarsawI11_SURVEY'] = surveys['factorsPublicTransportWarsawI11_SURVEY'].astype(bool)
    # surveys['factorsPublicTransportWarsawI11_SURVEY'] = surveys['factorsPublicTransportWarsawI11_SURVEY'].astype(bool)
    # surveys['driving1leDiscouragesCycling_SURVEY'] = surveys['driving1leDiscouragesCycling_SURVEY'].astype(bool)
    #
    # surveys['avgPeriod_TRANSIT'] = surveys['avgPeriod_TRANSIT'].astype(float)
    # surveys['avgBusTime_TRANSIT'] = surveys['avgBusTime_TRANSIT'].astype(float)
    # surveys['avgTramTime_TRANSIT'] = surveys['avgTramTime_TRANSIT'].astype(float)
    # surveys['minDistanceGrowth_TRANSIT'] = surveys['minDistanceGrowth_TRANSIT'].astype(float)
    # surveys['Speed_CAR'] = surveys['Speed_CAR'].astype(float)
    # surveys['avgTransfersNumber_TRANSIT'] = surveys['avgTransfersNumber_TRANSIT'].astype(float)
    # surveys['Speed_WALK'] = surveys['Speed_WALK'].astype(float)
    # surveys['avgWaitingTime_TRANSIT'] = surveys['avgWaitingTime_TRANSIT'].astype(float)
    # surveys['minSpeed_TRANSIT'] = surveys['minSpeed_TRANSIT'].astype(float)
    # surveys['avgSpeed_TRANSIT'] = surveys['avgSpeed_TRANSIT'].astype(float)
    # surveys['maxSpeed_TRANSIT'] = surveys['maxSpeed_TRANSIT'].astype(float)
    # surveys['avgStops_TRANSIT'] = surveys['avgStops_TRANSIT'].astype(float)

    # surveys['ElevationLost_WALK'] = surveys['ElevationLost_WALK'].astype(float)
    # surveys['ElevationGained_WALK'] = surveys['ElevationGained_WALK'].astype(float)
    #
    # surveys.bicycleMainReason_SURVEY = surveys.bicycleMainReason_SURVEY.fillna('')
    # surveys.safetyCar_SURVEY = surveys.safetyCar_SURVEY.fillna('')
    # surveys.safetyBicycle_SURVEY = surveys.safetyBicycle_SURVEY.fillna('')
    # surveys.safetyPublicTransport_SURVEY = surveys.safetyPublicTransport_SURVEY.fillna('')
    # surveys.safetyWalking_SURVEY = surveys.safetyWalking_SURVEY.fillna('')
    # surveys.transport_SURVEY = surveys.transport_SURVEY.fillna('')

    # arff.dump('CITIZENS_W1_W2_5_1_1_fixed_merged(in)_with_vistula_district_and_bank.arff', surveys.values, names=surveys.columns, relation='warsaw')

    # Identify class attribute
    # class_attr = 'travelAggregation'

    # relation = "surveys"
    #
    # with open("surveys.arff", "w", encoding="utf8") as f:
    #     f.write(f"@RELATION \"{relation}\"\n")
    #
    #     for col in surveys.columns:
    #         dtype = surveys[col].dtype
    #
    #         if dtype == 'object':
    #             print(col)
    #             attributes = list(surveys[col].unique())
    #             cleaned_list = [x for x in attributes if not (isinstance(x, float) and math.isnan(x))]
    #
    #             result = ', '.join(cleaned_list)
    #             f.write(f"@ATTRIBUTE {col} {{{result}}}\n")
    #         elif dtype == 'float64':
    #             f.write(f"@ATTRIBUTE {col} numeric\n")
    #         elif dtype == 'int64':
    #             f.write(f"@ATTRIBUTE {col} numeric\n")
    #         elif dtype == 'bool':
    #             f.write(f"@ATTRIBUTE {col} {{True, False}}\n")
    #         else:
    #             f.write(f"@ATTRIBUTE {col} string\n")
    #
    #     f.write('\n')
    #     f.write('@DATA\n')
    #
    #     for index, row in surveys.iterrows():
    #         for i, col in enumerate(surveys.columns):
    #             val = row[col]
    #             # Check if this is the last column
    #             if i == len(surveys.columns) - 1:
    #                 if pd.isna(val):
    #                     f.write(f"?")  # No comma after last col
    #                 else:
    #                     f.write(f"{val}")  # No comma after last col
    #             else:
    #                 if pd.isna(val):
    #                     f.write(f"?,")
    #                 else:
    #                     f.write(f"{val},")
    #
    #         f.write('\n')
