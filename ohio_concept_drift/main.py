import pandas
import numpy as np

from ohio_concept_drift.ohio_data import plot_ohio, load_ohio_data_per_experiment, plot_usa, load_usa_data_per_experiment
from ohio_concept_drift.warsaw_data import plot_warsaw
from ohio_concept_drift.latex import latex_usa
from ohio_concept_drift.warsaw_arff import arff_warsaw_surveys
from ohio_concept_drift import moran
from ohio_concept_drift import config
from ohio_concept_drift import detection_summary


def task_plot_ohio():
    plot_ohio('NB_ADWIN', 'experiments/Ohio/Eksperyment 2 NB ADWIN HDDM pełne przebiegi/Eksperyment_2/NB_ADWIN')
    plot_ohio('NB_HDDM_ONESIDED', 'experiments/Ohio/Eksperyment 2 NB ADWIN HDDM pełne przebiegi/Eksperyment_2/NB_HDDM_ONESIDED')

    plot_ohio('SRP_HDDM_ONESIDED', 'experiments/Ohio/Eksperyment 3 SRP HDDM pełne przeliczenie/SRP_HDDM_ONESIDED')

    plot_ohio('ARF_ADWIN', 'experiments/Ohio/Eksperyment 4/ARF_ADWIN')
    plot_ohio('HAT_ADWIN', 'experiments/Ohio/Eksperyment 4/HAT_ADWIN')
    plot_ohio('HT_ADWIN', 'experiments/Ohio/Eksperyment 4/HT_ADWIN')
    plot_ohio('HT_HDDM_ONESIDED', 'experiments/Ohio/Eksperyment 4/HT_HDDM_ONESIDED')

    plot_ohio('ARF_HDDM_ONESIDED', 'experiments/Ohio/ARF_HDDM_ONESIDED')


def task_plot_usa():
    plot_usa('', '')


def task_prepare_latex_ohio_table():
    column_name = 'total_drift_detection'
    NB_ADWIN = load_ohio_data_per_experiment('NB_ADWIN', 'experiments/Ohio/Eksperyment 2 NB ADWIN HDDM pełne przebiegi/Eksperyment_2/NB_ADWIN', column_name)
    NB_HDDM_ONESIDED = load_ohio_data_per_experiment('NB_HDDM_ONESIDED',
                                               'experiments/Ohio/Eksperyment 2 NB ADWIN HDDM pełne przebiegi/Eksperyment_2/NB_HDDM_ONESIDED', column_name)

    SRP_HDDM_ONESIDED = load_ohio_data_per_experiment('SRP_HDDM_ONESIDED', 'experiments/Ohio/Eksperyment 3 SRP HDDM pełne przeliczenie/SRP_HDDM_ONESIDED',
                                                      column_name)

    # moran.usa_moran_correlation(results_config=config.usa_results_config)
    # moran.usa_moran_latex(results_config=config.usa_results_config, target_directory='usa')


def task_plot_warsaw():
    plot_warsaw()


def task_basic_statistic_latex():
    # latex_warsaw()
    # latex_ohio()
    latex_usa()


def task_warsaw_arff():
    arff_warsaw_surveys()


# moran.ohio_moran_correlation()
# task_basic_statistic_latex()
# task_plot_usa()
task_plot_ohio()
# task_warsaw_arff()

# task_plot_ohio()
# plot_warsaw()

# latex_warsaw()
# task_prepare_latex_table()
