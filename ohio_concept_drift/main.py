from ohio_concept_drift.warsaw_surveys import assign_district_and_vistula_bank
from ohio_concept_drift.ohio_data import plot_ohio
from ohio_concept_drift.warsaw_data import plot_warsaw
from ohio_concept_drift.latex import latex_ohio, latex_warsaw
import arff


def task_plot_ohio():
    plot_ohio('NB_ADWIN', 'experiments/Ohio/Eksperyment 2 NB ADWIN HDDM pełne przebiegi/Eksperyment_2/NB_ADWIN')
    plot_ohio('NB_HDDM_ONESIDED', 'experiments/Ohio/Eksperyment 2 NB ADWIN HDDM pełne przebiegi/Eksperyment_2/NB_HDDM_ONESIDED')

    plot_ohio('SRP_HDDM_ONESIDED', 'experiments/Ohio/Eksperyment 3 SRP HDDM pełne przeliczenie/SRP_HDDM_ONESIDED')

    plot_ohio('ARF_ADWIN', 'experiments/Ohio/Eksperyment 4/ARF_ADWIN')
    plot_ohio('HAT_ADWIN', 'experiments/Ohio/Eksperyment 4/HAT_ADWIN')
    plot_ohio('HT_ADWIN', 'experiments/Ohio/Eksperyment 4/HT_ADWIN')
    plot_ohio('HT_HDDM_ONESIDED', 'experiments/Ohio/Eksperyment 4/HT_HDDM_ONESIDED')

    plot_ohio('ARF_HDDM_ONESIDED', 'experiments/Ohio/ARF_HDDM_ONESIDED')


def task_plot_warsaw():
    plot_warsaw()


def task_ohio_latex():
    latex_warsaw()
    latex_ohio()


def district_and_vistula_bank():
    warsaw_surveys = assign_district_and_vistula_bank()

    # Get columns starting with '***'
    surveys = warsaw_surveys[
        [col for col in warsaw_surveys.columns if col.endswith(('_SURVEY', '_TRANSIT', '_WALK', '_CAR')) and not col.endswith('_LOW_TRANSIT')]]
    surveys.loc[:, "label"] = warsaw_surveys.loc[:, "transport_SURVEY"]

    categorical_cols = [col for col in warsaw_surveys.columns if col.startswith(('beliefsWarsaw', 'occupationMain', 'opinions'))]
    surveys[categorical_cols] = surveys[categorical_cols].astype('category')
    surveys['monthOfBirth_SURVEY'] = surveys['monthOfBirth_SURVEY'].astype('category')

    surveys = surveys.drop(columns=[
        "homeAddressGeocoding_SURVEY",
        "startingAddressGeocoding_SURVEY",
        "localisationGeocoding_SURVEY",
        "cnPath_WALK",
        "cnPath_CAR",
        "cnPath_TRANSIT",
        "cnTransportModes_WALK",
        "PlanType_TRANSIT",
        "PlanType_WALK",
        "PlanType_WALK",
        "cnTransportModes_TRANSIT",
        "FirstStopName_TRANSIT",
        "FirstStopGeocoding_TRANSIT",

        "ParkingCost_CAR",
        "minCost_TRANSIT",
        "avgCost_TRANSIT",
        "maxCost_TRANSIT"
    ], axis='columns')

    arff.dump('CITIZENS_W1_W2_5_1_1_fixed_merged(in)_with_vistula_district_and_bank.arff', surveys.values, names=surveys.columns, relation='warsaw')

    surveys.to_csv('resources/CITIZENS_W1_W2_5_1_1_fixed_merged(in)_with_vistula_district_and_bank.csv', encoding='UTF-8', sep=';', decimal='.', index=False)
