import numpy as np

from ohio_concept_drift.warsaw_surveys import assign_district_and_vistula_bank
import csv2arff
import argparse
import csv


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
        "loca11ationGeocoding_SURVEY",
        "FirstStopGeocoding_TRANSIT"
    ], axis='columns')

    surveys = surveys[['sex_SURVEY'] + [col for col in surveys.columns if col != 'sex_SURVEY']]

    surveys.replace([np.inf, -np.inf], 0, inplace=True)

    surveys.fillna({
        'ParkingCost_CAR': 0.0,
        'ParkingDifficultyIntersectionArea_CAR': 0.0,
        'ParkingDifficultyIntersectionCentroid_CAR': 0.0,
        'ParkingDifficultyZoneCentroid_CAR': 0.0,
        'yearOfBirth_SURVEY': 0.0,
        'homeAddressLatitude_SURVEY': 0.0,
        'homeAddressLongitude_SURVEY': 0.0,
        'startingAddressLatitude_SURVEY': 0.0,
        'startingAddressLongitude_SURVEY': 0.0,
        'FirstStopLatitude_TRANSIT': 0.0,
        'FirstStopLongitude_TRANSIT': 0.0,
        'childrenNumber_SURVEY': 0,
        'usingCar_SURVEY': False,
        'parking_SURVEY': False,
        'carsNumber_SURVEY': 0,
        'scooterNumber_SURVEY': 0,
        'bicycleNumber_SURVEY': 0,
        'motorNumber_SURVEY': 0,
        'householdMembers_SURVEY': 0,
        'parkingTime_SURVEY': 0,
        'Routes_CAR': 0,
        'Duration_CAR': 0,
        'Distance_CAR': 0,
        'Speed_CAR': 0,
        'WalkDistance_CAR': 0,
        'WalkDuration_CAR': 0,
        'DistanceGrowth_CAR': 0,
        'DurationInTraffic_CAR': 0,
        'SpeedInTraffic_CAR': 0,

        'factorsPublicTransportWarsawI1_SURVEY': "NO RESPONSE",
        'factorsPublicTransportWarsawI2_SURVEY': "NO RESPONSE",
        'factorsPublicTransportWarsawI3_SURVEY': "NO RESPONSE",
        'factorsPublicTransportWarsawI4_SURVEY': "NO RESPONSE",
        'factorsPublicTransportWarsawI5_SURVEY': "NO RESPONSE",
        'factorsPublicTransportWarsawI6_SURVEY': "NO RESPONSE",
        'factorsPublicTransportWarsawI7_SURVEY': "NO RESPONSE",
        'factorsPublicTransportWarsawI8_SURVEY': "NO RESPONSE",
        'factorsPublicTransportWarsawI9_SURVEY': "NO RESPONSE",
        'factorsPublicTransportWarsawI10_SURVEY': "NO RESPONSE",
        'factorsPublicTransportWarsawI11_SURVEY': "NO RESPONSE",
        'factorsPublicTransportWarsawI12_SURVEY': "NO RESPONSE",
        'factorsPublicTransportWarsawI13_SURVEY': "NO RESPONSE",
        'factorsPublicTransportWarsawI14_SURVEY': "NO RESPONSE",
        'factorsPublicTransportWarsawI15_SURVEY': "NO RESPONSE",
        'factorsPublicTransportWarsawI16_SURVEY': "NO RESPONSE",

        'journeyReasonsWarsawI16_SURVEY': "NO RESPONSE",

        'district': "OUT OF CITY",
        'vistula_bank': "OUT OF CITY",

        'minBusTime_TRANSIT': 0,
        'avgBusTime_TRANSIT': 0,
        'maxBusTime_TRANSIT': 0,
        'minBusShare_TRANSIT': 0,
        'avgBusShare_TRANSIT': 0,
        'maxBusShare_TRANSIT': 0,
        'minTramTime_TRANSIT': 0,
        'avgTramTime_TRANSIT': 0,
        'maxTramTime_TRANSIT': 0,
        'minTramShare_TRANSIT': 0,
        'avgTramShare_TRANSIT': 0,
        'maxTramShare_TRANSIT': 0,
        'minRailTime_TRANSIT': 0,
        'avgRailTime_TRANSIT': 0,
        'maxRailTime_TRANSIT': 0,
        'minRailShare_TRANSIT': 0,
        'avgRailShare_TRANSIT': 0,
        'maxRailShare_TRANSIT': 0,
        'minSubwayTime_TRANSIT': 0,
        'avgSubwayTime_TRANSIT': 0,
        'maxSubwayTime_TRANSIT': 0,
        'minSubwayShare_TRANSIT': 0,
        'avgSubwayShare_TRANSIT': 0,
        'maxSubwayShare_TRANSIT': 0,
        'minDistanceGrowth_TRANSIT': 0,
        'avgDistanceGrowth_TRANSIT': 0,
        'maxDistanceGrowth_TRANSIT': 0,

        'bicycleMainReason_SURVEY': "NO RESPONSE",
        'safetyCar_SURVEY': "NO RESPONSE",
        'safetyBicycle_SURVEY': "NO RESPONSE",
        'safetyPublicTransport_SURVEY': "NO RESPONSE",
        'safetyWalking_SURVEY': "NO RESPONSE",
        'driving1leDiscouragesCycling_SURVEY': "NO RESPONSE",

        'Routes_WALK': 0,
        'Distance_WALK': 0,
        'Duration_WALK': 0,
        'Speed_WALK': 0,
        'ElevationLost_WALK': 0,
        'ElevationGained_WALK': 0,
        'DistanceGrowth_WALK': 0,
        'Routes_TRANSIT': 0,

        'minStops_TRANSIT': 0,
        'avgStops_TRANSIT': 0,
        'maxStops_TRANSIT': 0,
        'minDistance_TRANSIT': 0,
        'avgDistance_TRANSIT': 0,
        'maxDistance_TRANSIT': 0,
        'minWalkDistance_TRANSIT': 0,
        'avgWalkDistance_TRANSIT': 0,
        'maxWalkDistance_TRANSIT': 0,
        'minWalkDuration_TRANSIT': 0,
        'avgWalkDuration_TRANSIT': 0,
        'maxWalkDuration_TRANSIT': 0,
        'minWaitingTime_TRANSIT': 0,
        'avgWaitingTime_TRANSIT': 0,
        'maxWaitingTime_TRANSIT': 0,
        'minDuration_TRANSIT': 0,
        'avgDuration_TRANSIT': 0,
        'maxDuration_TRANSIT': 0,
        'minSpeed_TRANSIT': 0,
        'avgSpeed_TRANSIT': 0,
        'maxSpeed_TRANSIT': 0,
        'minTransfersNumber_TRANSIT': 0,
        'avgTransfersNumber_TRANSIT': 0,
        'maxTransfersNumber_TRANSIT': 0,
        'minTransitTime_TRANSIT': 0,
        'avgTransitTime_TRANSIT': 0,
        'maxTransitTime_TRANSIT': 0,
        'minPeriod_TRANSIT': 0,
        'avgPeriod_TRANSIT': 0,
        'maxPeriod_TRANSIT': 0,
        'minCost_TRANSIT': 0,
        'avgCost_TRANSIT': 0,
        'maxCost_TRANSIT': 0

    }, inplace=True)

    cols_with_na = surveys.columns[surveys.isna().any()].tolist()

    csv_file_name = 'CITIZENS_W1_W2_5_1_1_fixed_merged(in)_with_vistula_district_and_bank'
    surveys.to_csv(f"resources/{csv_file_name}.csv", encoding='UTF-8', sep=',', decimal='.', quotechar='"', quoting=csv.QUOTE_MINIMAL, index=False)

    args = argparse.Namespace(
        input=f"resources/{csv_file_name}.csv",
        output=f"resources/{csv_file_name}.arff",
        name="warsaw_surveys",
        delimiter=','
    )

    csv2arff.Csv2Arff(args)
