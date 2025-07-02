from ohio_concept_drift.warsaw_surveys import assign_district_and_vistula_bank
from ohio_concept_drift.ohio_data import plot_ohio


def task_plot_ohio():
    plot_ohio()


def district_and_vistula_bank():
    warsaw_surveys = assign_district_and_vistula_bank()
    warsaw_surveys.to_csv('resources/CITIZENS_W1_W2_5_1_1_fixed_merged(in)_with_vistula_district_and_bank.csv', encoding='UTF-8', sep=';', decimal='.',
                          index=False)


task_plot_ohio()
