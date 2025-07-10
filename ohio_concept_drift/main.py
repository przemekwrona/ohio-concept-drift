from ohio_concept_drift.ohio_data import plot_ohio
from ohio_concept_drift.warsaw_data import plot_warsaw
from ohio_concept_drift.latex import latex_ohio, latex_warsaw
from ohio_concept_drift.warsaw_arff import arff_warsaw_surveys


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


def task_warsaw_arff():
    arff_warsaw_surveys()


task_warsaw_arff()

# task_plot_ohio()
# plot_warsaw()

# latex_warsaw()
